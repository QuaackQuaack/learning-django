from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

class SignUpPageTest(TestCase):

    def test_url_exist_at_correct_location_signup(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_viewpage(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(
                reverse("signup"),
                {
                    "username":"testuser",
                    'email':"testuser@email.com",
                    'password1': 'testpass134',
                    'password2': 'testpass134',
                    },
                )
        self.assertEqual(response.status_code, 302)#after singup it will be redirect so we use 302
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@email.com')

                    

        

        

