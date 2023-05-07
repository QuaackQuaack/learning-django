from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
                username = "agoodname", email = "ok@ok.com", password = "test")

        cls.post = Post.objects.create(
                title = "a good title",
                body = "a good body",
                author = cls.user,)

    def test_model(self):
        self.assertEqual(self.post.title, "a good title")
        self.assertEqual(self.post.body , "a good body")
        self.assertEqual(self.post.author.username, "agoodname")
        self.assertEqual(str(self.post), "a good title")
        self.assertEqual(self.post.get_absolute_url(), "/1/")

    def test_url_exist(self):
        response = self.client.get("/") #listview
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/1/") #detail view url 
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "a good title") #here you can keep anything within that template
    
    def test_page(self):
        response = self.client.get(reverse("page", kwargs= {"pk" : self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'page.html')
        self.assertContains(response , 'a good body')





