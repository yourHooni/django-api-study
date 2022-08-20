"""
    Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTests(TestCase):
    """Test models."""
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'admin@dev.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'admin@DEV.com'
        password = 'test123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email = 'admin@gmail.com'
        password = 'test123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertEqual(user.is_superuser, True)
        self.assertTrue(user.is_staff, True)
