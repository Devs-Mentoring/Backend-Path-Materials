from django.shortcuts import render
from .models import Article


def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
