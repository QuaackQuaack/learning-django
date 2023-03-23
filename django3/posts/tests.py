from django.test import TestCase
from .models import Post
# Create your tests here.

class PostModelsTest(TestCase):
    def setUp(self):# we just create sample of database and check it
        Post.objects.create(text='just a text') # here we create sample

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a text')
