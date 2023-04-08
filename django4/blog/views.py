from django.shortcuts import render
from .models import Post
from django.views.generic import ListView , DetailView 
# Create your views here.

class BlogPageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_view'

class BlogDetailView(DetailView): # this is to view blog in detail and mainly used in  slug or primary key 
    model = Post # WE can't give path in detailView , mostly detail view use primay key or slug 
    template_name = 'post_detail.html'
    context_object_name = 'all_detail_view' #without this line, we need to use either model or object as -
                                            #context object name. 

