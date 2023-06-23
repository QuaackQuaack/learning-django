
from django.urls import path
from .views import HomePageView, TemplatePageView, GreetPageView

urlpatterns = [
        path("template/<str:name>/", GreetPageView.as_view(), name = 'greet'),
        path("<str:name>/", HomePageView.as_view(), name = "home"),
        path("template/templates", TemplatePageView.as_view(), name = 'template') 
        ]
