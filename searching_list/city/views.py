from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from django.db.models import Q #complex query set that act as OR

from .models import City
# Create your views here.

class HomePageView(TemplateView):
    model = City
    template_name = 'home.html'


class SearchPageView(ListView):
    model = City
    template_name = 'search_result.html'

    def get_queryset(self):
        #query = self.request.GET("q")#this will only give us dictionary value, to get key we use GET.get
        query = self.request.GET.get("q")
        object_list = City.objects.filter(
                Q(name = query) | Q(state = query) 
                )
        return object_list

        



    

