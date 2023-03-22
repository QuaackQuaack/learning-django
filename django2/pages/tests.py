#from django.test import TestCase # we use this while we are using actual data base 
from django.test import SimpleTestCase # we use this since we are not using any data base

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) # here 200 is standard response for successfull http request
#assertEqual check whether response.status_code == 200 or not
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
