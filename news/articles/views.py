from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #to control the authorization.
from djanog.contrib.auth.mixins import UserPassesTestMixin #provide permission to author only to edit and update page
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Article
# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article_list.html'
    model = Article
    custom_user_name = 'articlelist'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article_detail.html'
    model = Article
    custom_user_name = 'articledetail'

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView): #oder of passing attributes  matter
    template_name = 'article_edit.html'
    model = Article
    fields = ( 'title', 'body' )

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user

#UserPassesTestMixin checks whether the login user and author is same or not 

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list') #redirect to home page

    def test_fun(self): #this method is used by UserPassesTestMixin 
        obj = self.get_object() #getobject help us to get slug or pk.
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView): #after adding LoginRequiredMixin we can direct ourself to login page
    model = Article                                      #unauthorized person will be directed to login page directly.
    template_name = 'article_new.html'
    fields = ('title', 'body')

    def form_valid(self,form): #this method is to set login user, to author of article without filling form
        form.instance.author = self.request.user 
        return super().form_valid(form)
