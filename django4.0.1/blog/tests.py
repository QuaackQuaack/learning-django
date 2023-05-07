from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
                username = 'agoodname', email = "ok@ok.com", password = "password" )
        
        cls.post = Post.objects.create(
                title = "a good title",
                body = "a good body",
                author = cls.user
                )

    def test_post_model(self):
        self.assertEqual(self.post.title, "a good title")
        self.assertEqual(self.post.body, "a good body")
        self.assertEqual(self.post.author.username, "agoodname")
        self.assertEqual(str(self.post), 'a good title')
        self.assertEqual(self.post.get_absolute_url(), "/1/")
    
    def test_url_exit_at_correct(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_module(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "a good body")

    def test_body_module(self):
        response = self.client.get(reverse('page', kwargs = {"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page.html')
        self.assertContains(response, 'a good title')

    def test_post_createview(self):
        response = self.client.post(
                reverse("create"),
                {
                    "title": "new title",
                    "body": "new body",
                    "author": self.user.id }
                )
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "new title")
        self.assertEqual(Post.objects.last().body, "new body")


    def test_post_updateview(self):
        response = self.client.post(
                reverse('update', args = "1"),{
                    'title':'edit title',
                    'body': 'edit body',
                    }
                )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'edit title')
        self.assertEqual(Post.objects.last().body, 'edit body')

    def test_post_deleteview(self):
        response = self.client.post(reverse('delete', args = '1'))
        self.assertEqual(response.status_code, 302)







