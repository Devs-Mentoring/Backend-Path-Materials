from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/delete_confirm.html'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author