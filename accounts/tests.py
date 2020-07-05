from django.test import TestCase
from posts.models import Post
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your tests here.


class TestSignUp(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.username = "user_name"
        self.email = "soos@i.com"
        self.password = "vvggtt"

    def test_signup(self):
        # Create an instance of a POST request.
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/signup.html')

    def test_signup_form(self):
        "ToDo: How to do proper testing of signup?"
        data = {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }
        # form = UserCreationForm(data = data)
        response = self.client.post("/accounts/signup/", data=data)
        self.assertRedirects(response, '/posts', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)

class TestLogin(TestCase):
    '''
    Tests for Login
    '''
    pass

class TestLogout(TestCase):
    '''
    Tests for Logout
    '''
    pass