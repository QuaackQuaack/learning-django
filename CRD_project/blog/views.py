from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView #there are four type of edit 
#simply following CRUD principal i.e. Create, view, update, delete.  
# Register your models here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_page_view'

class AllPageView(DetailView):
    model = Post
    template_name = 'page.html'
    context_object_name = 'all_page_data'

class NewPageView(CreateView):
    model = Post
    template_name = 'new_page.html'
    fields = ['title','author','body'] #with fields, we set database which we want to exposse like title , author and body in this case

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

