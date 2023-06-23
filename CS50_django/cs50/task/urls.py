from django.urls import path

from .views import ListPageView, CreatePageView
#from .views import TaskPageView, CreatePageView 
urlpatterns = [
        path("task/", ListPageView.as_view(), name = 'tasks'),
        path("task/new/", CreatePageView.as_view(), name = 'new_task'),
        #path("task/", TaskPageView.as_view(), name = 'tasks')
        ]
