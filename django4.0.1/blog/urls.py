from django.urls import path

from .views import (HomePageView, 
                    BlogPageView, 
                    BlogCreateView, 
                    BlogDeleteView,
                    BlogUpdateView)

urlpatterns = [
        path("", HomePageView.as_view(), name = 'home'),
        path("<int:pk>/", BlogPageView.as_view(), name = 'page'),
        path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name = 'update'),
        path("post/create/", BlogCreateView.as_view(), name = 'create'),
        path("post/<int:pk>/delete", BlogDeleteView.as_view(), name = 'delete'),

        ]
