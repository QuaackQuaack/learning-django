from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
            'auth.User',
            on_delete = models.CASCADE )
    body = models.TextField()

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('page', kwargs = {"pk":self.pk})
