from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePageView(View):
    
    def get(self,request,name):
        return HttpResponse(f"hello, {name.capitalize()}")

class TemplatePageView(TemplateView):
    template_name = 'home.html'

def greet(request, name):
    return render(request, "../templates/greet.html", {"name": name.capitalize()})
