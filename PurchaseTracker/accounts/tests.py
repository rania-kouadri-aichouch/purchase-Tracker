from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# test for user registration 

class UserRegistrationViewTest(TestCase):
    def test_user_registration(self):
        client = Client()
        data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = client.post(reverse('register'), data)
        
        # Check redirect
        self.assertRedirects(response, reverse('login'))

        # Check if user added to database
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)


# test for login
class UserLoginViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_user_login(self):
        client = Client()
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        response = client.post(reverse('login'), data)

        # Check the redirect
        self.assertRedirects(response, reverse('landing'))

        # Check if the user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)


# logout test

class UserLogoutViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_user_logout(self):
        client = Client()
        # Login the user
        client.login(username='testuser', password='testpassword123')
        response = client.get(reverse('logout'))

        # Check if the redirect works
        self.assertRedirects(response, reverse('login'))

        # Check if the user is not authenticated after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)
