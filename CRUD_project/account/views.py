from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy 
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') #class attribute are evaluated while importing class so to prevent
    template_name = 'registration/signup.html' #from early evaluation it is used 
#with SignUp we have different built-in 'flash message'
