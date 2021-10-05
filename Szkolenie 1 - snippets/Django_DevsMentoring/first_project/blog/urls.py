from django.contrib import admin
from django.urls import path
from . import views
from .views import ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about')
]