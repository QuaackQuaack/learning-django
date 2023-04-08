from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
            'auth.User', # here to we need to put author name as a default but through change in field we can also keep it blank
             #blank = True , # to post without author name  #using null is bad idea cuz next one can also be null and make error
            on_delete = models.CASCADE, )
    body = models.TextField()

    def __str__(self):
        return self.title
