"""
    Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from recipe.models import Tag
from recipe.serializers import TagSerializer

TAGS_URL = reverse('recipe:tag-list')


class PublicIngredientsApiTests(TestCase):
    """Test the publicly available ingredients API"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required to access the endpoint."""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
                    email='test@test.com',
                    password='test1234'
                )
        self.client.force_authenticate(self.user)

    def test_retrieve_tag_list(self):
        """Test retrieving a list of tags."""
        Tag.objects.create(user=self.user, name='Test tag1')
        Tag.objects.create(user=self.user, name='Test tag2')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-created_at')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test that tags for the authenticated user are returned."""
        user2 = get_user_model().objects.create_user(
            email='test2@test.com',
            password='test1234'
        )

        Tag.objects.create(user=user2, name='User2 Tag')
        tag = Tag.objects.create(user=self.user, name='User1 Tag')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_create_tag_invalide_tag_successful(self):
        """Test creating a new tag."""
        payload = {'name': "Test tag"}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(
            user=self.user,
            name=payload['name']
        )
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload."""
        payload = {'name': ''}
        res = self.client.post(TAGS_URL, **payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
