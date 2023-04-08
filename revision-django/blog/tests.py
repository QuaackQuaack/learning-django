from django.test import TestCase
from django.contrib.auth import get_user_model #it reference our active user
from django.urls import reverse

from .models import Post
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username = 'testuser',
                email = 'test@email.com',
                password = 'secret' )
        
        self.post = Post.objects.create(
                title = 'A good title',
                body = 'nice body content',
                author = self.user, )
       
    def test_string_representation(self): #This check the str returing part of model
        post = Post(title = 'A sample title')
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self): #this check content part like author , title and body
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','nice body content')

    def test_post_list_view(self): #this one is for view  and template both 
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('post/100000/') #this is to set limit
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')



