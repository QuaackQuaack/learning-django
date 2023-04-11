from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView #there are four type of edit 
#simply following CRUD principal i.e. Create, view, update, delete.  

from django.urls import reverse_lazy #this is opposite of reverse()
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
    context_object_name = 'edit_page'

class  BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home') #reverse_lazy returns object, 
    #reverse_lazy is done in Class based because class are evaluated on import and to resolve URL not found
    #we use reverse_lazy 

    #reverse is used in function based because we have URLConfig at the time of function calling
    
