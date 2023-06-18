from django.urls import path

from .views import HomePageView, SearchPageView

urlpatterns = [
        path("", HomePageView.as_view(), name= 'home'),
        path("search/", SearchPageView.as_view(), name = 'search')

        ]

