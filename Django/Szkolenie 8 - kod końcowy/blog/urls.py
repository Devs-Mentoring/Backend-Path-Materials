from django.contrib import admin
from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article-update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article-delete')
]