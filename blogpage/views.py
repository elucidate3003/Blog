from django.shortcuts import render,get_object_or_404
from .models import Blog_page

# Create your views here.

def home(request):
  blogs = Blog_page.objects.all().order_by('-published_on')
  if len(blogs) > 5:
    blogs = blogs[:5]

  context ={
    'blogs' : blogs,
  }
  return render(request,'main/blogpage.html',context)

def each_article(request,slug):
  article = get_object_or_404(Blog_page,slug=slug)
  body = article.body.split('\n')
  context={
    'article' : article,
    'body' : body
  }
  return render(request,'main/article.html',context)

def contact_us(request):
    return render(request, 'main/contact_us.html')

def about(request):
  return render(request,'main/about.html')

def search_article(request):
    if request.method == 'POST':
        search_text = request.POST.get('searched')
    else:
        search_text = ''
    articles = Blog_page.objects.filter(title__icontains=search_text)
    # slugs = [i.slug for i in articles]
    context = {
        'blogs': articles,
        # 'slugs': slugs
    }
    return render(request, 'main/blogpage.html', context)