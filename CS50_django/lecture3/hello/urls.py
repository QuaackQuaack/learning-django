from django.urls import path
from .views import index, brian, greet

urlpatterns = [
        path('', index, name = 'home'),
        path('brian/', brian, name = 'brian'),
        path("<str:name>/", greet, name = 'greet')
        ]
