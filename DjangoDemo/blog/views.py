from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    articles = models.Aritical.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Aritical.objects.get(pk=article_id)
    return render(request, 'blog/arcticle_page.html', {'article': article})

def edit_page(request, articel_id):
    if articel_id == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Aritical.objects.get(pk=articel_id)
    return render(request, 'blog/edit_page.html', {'article': article})

def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Aritical.objects.create(title = title, content = content)
    articals = models.Aritical.objects.all()
    return render(request, 'blog/index.html', {'articals': articals})