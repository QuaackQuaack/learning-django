from django.db import models 

# Create your models here.

class Post(models.Model): # here we have created database model called Post
    text = models.TextField() # it stores text 
