from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomePageView(View):
    
    def get(self,request,name):
        return HttpResponse(f"hello, {name.capitalize()}")

class TemplatePageView(TemplateView):
    template_name = 'home.html'

class GreetPageView(View):
        def get(self,request, name):
            context = {
                        "name": name.capitalize() } 
            return render(request, "../templates/greet.html", context)
