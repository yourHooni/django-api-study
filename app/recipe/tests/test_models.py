"""
    Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from recipe.models import Tag


def sample_user(email="test1@test.com", password="test1234"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class TagTests(TestCase):
    def test_tag_string(self):
        """Test the tag string representation."""
        tag = Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
