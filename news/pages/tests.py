from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class HomePageView(TestCase):

    def test_url_exits_at_current_location_homepageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')

