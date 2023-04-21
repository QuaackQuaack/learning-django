#note ;- we don't need to check inbuilt function of django like str, get_absolute_url
#self.client exist in TestCase only.
#self.client create httpRequest object and passes it through request process
from django.test import TestCase
from django.contrib.auth import get_user_model #this will return current active user instead of using USER
from django.urls import reverse


from .models import Post
# Create your tests here.
'''at first you need to create a user ( self.user ) and then a content (self.post) and test that '''

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username = 'a good name',
                email = 'ok@ok.com',
                password = 'secret key')

        self.post = Post.objects.create(
                title = 'A good title',
                body = 'nice body content',
                author = self.user, )
   
    def test_string_representation(self): #to test __str__ function which return str title
        post = Post(title = 'A sample of title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self): # to test get_asbolute_url
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    #to test content of the blog, where we compare post(object we created to 
    def test_post_content(self): 
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.author}', 'a good name')
        self.assertEqual(f'{self.post.body}', 'nice body content')
    
    #to test views like list,details we need to create a reponse 
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))#self.client make Httprequest and then get 'home' 
        self.assertEqual(response.status_code,200) #this to check status_code return by the server
        self.assertContains(response, 'nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'page.html')

    def test_create_blog(self): 
        response = self.client.post(reverse('new_page'),{
            'title':'New title',
            'body':'New body',
            'author': self.user.id,
            })
        self.assertEqual(response.status_code, 302) #302 is way of performing URL redirection 
        self.assertEqual(Post.objects.last().title, "New title") #to retrieve last and model
        self.assertEqual(Post.objects.last().body, "New body")

    def test_update_blog(self):
        response = self.client.post(reverse('page_edit',args = '1'), {
            'title':"new title",
            'body': "new body"
            })
        self.assertEqual(response.status_code, 302)


    def test_delete_blog(self):
        response = self.client.post(reverse('post_delete', args = '1')) #adding comma at last create error
        self.assertEqual(response.status_code, 302) #idk why wants to knoww








