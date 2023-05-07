from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'damn_bro'

class BlogPageView(DetailView):
    model = Post
    template_name = 'page.html'
    context_object_name = 'pagekodetail'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title','author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')

