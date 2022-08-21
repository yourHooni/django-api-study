from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

payload1 = {'email': 'test@test.com', 'password': 'test1234'}
payload2 = {'email': 'test2@test.com', 'password': 'test1234'}
payload3 = {'email': 'wrong@test.com', 'password': 'wrong'}
payload4 = {'email': 'wrong', 'password': ''}


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class UserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_token_for_user(self):
        """Test that a token is created for the user."""
        create_user(**payload1)
        res = self.client.post(TOKEN_URL, payload1)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given."""
        create_user(**payload1)
        res = self.client.post(TOKEN_URL, payload2)

        # self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist."""
        res = self.client.post(TOKEN_URL, payload3)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that email and password are required."""
        res = self.client.post(TOKEN_URL, payload4)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)