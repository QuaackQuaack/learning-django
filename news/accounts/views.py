from django.shortcuts import render
from django.contrib.auth.models import AbstractUser

# Create your views here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null= True, blank = True)
