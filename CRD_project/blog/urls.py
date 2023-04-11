from django.urls import path
from .views import HomePageView, AllPageView , NewPageView 

urlpatterns = [
        path('post/new/',NewPageView.as_view(), name = 'new_page'),
        path('',HomePageView.as_view(),name='home'),
        path('post/<int:pk>/',AllPageView.as_view(), name = 'post_detail')
        ]
