from django.urls import path
from .views import  wish

urlpatterns = [
        path('', wish, name = 'index')
        ]
