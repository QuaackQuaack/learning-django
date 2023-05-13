from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class TestBlog(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
                username = 'a good name', email = 'ok@ok.com', password = 'agood')
        
        cls.post = Post.objects.create(
                title = 'a good title',
                body = 'a good body',
                author = cls.user)

    def test_model_Post(self):
        self.assertEqual(self.post.title, "a good title")
        self.assertEqual(self.post.body, "a good body")
        self.assertEqual(self.post.author.username, 'a good name')
        self.assertEqual(str(self.post), 'a good title')
        self.assertEqual(self.post.get_absolute_url(), "/1/")

    def test_url_exit_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "a good title")

    def test_blog_page(self):
        response = self.client.get(reverse("page", kwargs = {"pk": self.post.id }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page.html')
        self.assertContains(response, 'a good body')

    def test_create_page(self):
        response = self.client.post(reverse('create'), {
            'title':'a new title',
            'body': 'a new body',
            'author': self.user.id }
                                       )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'a new title')
        self.assertEqual(Post.objects.last().body, 'a new body')
        
    def test_update_page(self):
        response = self.client.post(reverse('update', args = '1'),{
            'title':'updated one',
            'body':'updated body' }
                                       )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'updated one')
        self.assertEqual(Post.objects.last().body, 'updated body')

    def test_delete_page(self):
        response = self.client.post(reverse('delete', args = '1'))
        self.assertEqual(response.status_code, 302)



