from django.urls import path

from .views import HomePageView, BlogPageView

urlpatterns = [
        path("", HomePageView.as_view(), name = 'home'),
        path("<int:pk>/", BlogPageView.as_view(), name = 'page')

        ]
