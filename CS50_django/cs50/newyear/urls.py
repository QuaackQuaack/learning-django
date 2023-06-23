from django.urls import path
from .views import NewYearView

urlpatterns = [
        path("newyear/", NewYearView.as_view(), name = 'newyear')
        ]

