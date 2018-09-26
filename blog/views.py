from django.shortcuts import render
from . import models

def index(request):
    articles=models.Article.objects.all()
    return render(request,'index.html',{'articles':articles})
def article(request,id):
    article=models.Article.objects.get(pk=id)
    return render(request,'article.html',{'article':article})

def edit(request,id):
    article=models.Article.objects.get(pk=id)
    return render(request,'edit.html',{'article':article})

def edit_function(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    models.Article.objects.create(content=content,title=title)
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
