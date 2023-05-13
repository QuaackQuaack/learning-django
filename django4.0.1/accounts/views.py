from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

class SignUpView(CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy("login") #after load of template succes_url redirect us to 
                                        #login page
    template_name = "registration/signup.html"
    
