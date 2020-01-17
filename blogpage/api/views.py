from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blogpage.models import Blog_page
import json
from blogpage.api.serializer import Blog_pageSerializer

@api_view(['GET',])
def article_get_data(request, slug):
    try:
        article = Blog_page.objects.get(slug=slug)
    except Blog_page.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Blog_pageSerializer(article)
        return Response(serializer.data)

@api_view(['PUT',])
def article_update_data_view(request, slug):
    try:
        article = Blog_page.objects.get(slug=slug)
    except Blog_page.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        serializer = Blog_pageSerializer(article, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Data updated!"
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def article_add_data_view(request):
    
    article = Blog_page()
    if request.method == "POST":
        serializer = Blog_pageSerializer(article, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Data Added!"
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def search_get_data(request):
    try:
        articles = Blog_page.objects.all()
    except Blog_page.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        blogs = []
        for article in articles:
            serializer = Blog_pageSerializer(article)
            blogs.append(serializer.data)
        search_json = json.dumps(search)
        return Response(blogs)


        # search_json = json.dumps(search)
        # return Response(serializer.data)

@api_view(['DELETE',])
def article_delete_view(request, slug):
    try:
        article = Blog_page.objects.get(slug=slug)
    except Blog_page.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        operation = article.delete()
        data = {}
        if operation:
            data['success'] = "The Article is deleted!"
        else:
            data['failure'] = "The Article is not deleted!"
        return Response(data=data)
