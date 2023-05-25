from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #to control the authorization.
from django.contrib.auth.mixins import UserPassesTestMixin #provide permission to author only to edit and update page
from django.views.generic import ListView, DetailView, FormView
from django.views import View  #master view of all other views
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from djanog.views.generic.detail import SingleObjectMixin #helps in obeject retrieving and helps in URl parameter handling

from .forms import CommentForm 

from django.urls import reverse_lazy, reverse

from .models import Article
# Create your views here.

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article_list.html'
    model = Article
    custom_user_name = 'articlelist'

class CommentGet(DetailView):                   #to avoid mixing of detailview and mixins we are creating separate form to 
    template_name = 'article_detail.html'       #get comment and post comment, previous Detailview will be same for GetComment    
    model = Article
    #custom_user_name = 'articledetail'

    def get_context_data(self, **kwargs): #to add information to a template by updating context
        context = super().get_context_data(**kwargs) #django loads template only once for performance
        #add additional data to current context
        context["forms"] = CommentForm() #so here this function provides comment form data while template is loading
        return context 

class CommentPost():
    model = Article
    form_class = CommentForm
    template_name = 'article_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit = False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs = {"pk": article.pk})

class ArticleDetailView(LoginRequiredMixin, View): #this class combines both CommentPost and CommentGet under View
    def get(self, request, *args, **kwargs):
        #handles GET requests and instantiaties a blank version of the form
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


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
