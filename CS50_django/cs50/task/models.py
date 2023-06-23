from django.db import models

from django.urls import reverse

# Create your models here.

class Post(models.Model):
    task = models.CharField( max_length = 200)

    def get_absolute_url(self):
        return reverse("tasks")



