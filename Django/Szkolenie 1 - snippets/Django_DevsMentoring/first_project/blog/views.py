from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Article


def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']