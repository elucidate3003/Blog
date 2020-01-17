from rest_framework import serializers
from blogpage.models import Blog_page

class Blog_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_page
        fields = ['title', 'author', 'genre', 'body']