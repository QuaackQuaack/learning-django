from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'damn_bro'

class BlogPageView(DetailView):
    model = Post
    template_name = 'page.html'
    context_object_name = 'pagekodetail'

