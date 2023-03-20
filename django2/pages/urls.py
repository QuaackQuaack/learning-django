from django.urls import path # to provide power to our webpage
from .views import HomePageView # to import views ko file 
from .views import AboutPageView 
urlpatterns = [
        path('',HomePageView.as_view(), name ='home'),
        path('about/',AboutPageView.as_view(),name = 'about'),
        ]
# adding .as_view() because we are using Class-based views
