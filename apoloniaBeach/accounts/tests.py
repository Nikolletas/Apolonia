from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from apoloniaBeach.accounts.models import Profile, MyUser

User = get_user_model()


class CreateUserAndProfileTest(TestCase):

    def test_register_user_and_create_profile(self):
        self.client = Client()
        response = self.client.post('/accounts/register/', {
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'first_name': 'Test',
            'last_name': 'User',
            'nationality': 'Some nationality',
            'phone_number': '00000000',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Profile.objects.count(), 1)
