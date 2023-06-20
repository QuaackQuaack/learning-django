
from django.urls import path
from .views import HomePageView, TemplatePageView, greet

urlpatterns = [
        path("template/<str:name>/", greet, name = 'greet'),
        path("<str:name>/", HomePageView.as_view(), name = "home"),
        path("template/templates", TemplatePageView.as_view(), name = 'template') 
        ]
