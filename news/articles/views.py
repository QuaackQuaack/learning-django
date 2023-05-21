from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Article
# Create your views here.

class ArticleListView:
    template_name = 'article_list.html'
    model = Article
    custom_user_name = 'articlelist'

class ArticleDetailView:
    template_name = 'article_detail.html'
    model = Article
    custom_user_name = 'articledetail'

class ArticleUpdateView:
    template_name = 'article_edit.html'
    model = Article
    fields = ( 'title', 'body' )

class ArticleDeleteView:
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list') #redirect to home page

class ArticleCreateView:
    model = Article
    template_name = 'article_create.html'
    fields = ( 'author', 'title', 'body')

