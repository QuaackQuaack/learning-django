from django.urls import path
from .views import HomePageView, AllPageView , NewPageView ,BlogUpdateView, BlogDeleteView

urlpatterns = [
        path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name = 'post_delete'),
        path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name = 'page_edit'),
        path('post/new/',NewPageView.as_view(), name = 'new_page'),
        path('',HomePageView.as_view(),name='home'),
        path('post/<int:pk>/',AllPageView.as_view(), name = 'post_detail')
        ]
