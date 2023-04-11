from django.db import models
from django.urls import reverse #it provides us, reference of an object by its URL template name.

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
            'auth.User',
            on_delete = models.CASCADE, )
    body = models.TextField()

    def __str__(self):
        return self.title
#to tell django where to direct user after successfully submitting form
    def get_absolute_url(self): 
        return reverse('post_detail', args=[str(self.id)])
    #here reverse is used to get view name --> url 
    # reverse help use optimize our site , if there is anychange in URL in future. 
    # from post_detail , our URL get added post/int:pk , will change to post/2, post/3 and so on. 
    # get_absolute_url is to manage canonical url, (canonical URl is used in SEO optimization) 
    # but in context of django, canonical URL can be understood as Main url like post/ 
