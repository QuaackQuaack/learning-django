from django.urls import path
from .views import BlogPageView, BlogDetailView

urlpatterns = [
        path('', BlogPageView.as_view(), name = 'home'),
        path('post/<int:pk>/', BlogDetailView.as_view(), name ='post_detail'),
        ]

'''We are using DetailView in views so ani detailview doesn't pass, path like listview
detailview use either slug or primary key ani for each author, title , it add one primary
key . like here path('post/<int:pk>/') int:pk means integer primary key (1,2,3...) for 
each coloumn
now about url pattern, like first page , urls pattern will look like post/1/
and secon one post/2/ '''

