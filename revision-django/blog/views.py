from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogPageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_views'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'all_detail_views'
    




