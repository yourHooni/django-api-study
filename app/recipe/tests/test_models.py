"""
    Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

from recipe import models


def sample_user(email="test1@test.com", password="test1234"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class TagTests(TestCase):
    """ Test the tag model."""
    def test_tag_string(self):
        """Test the tag string representation."""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)


class IngredientTests(TestCase):
    """ Test the ingredient model."""
    def test_ingredient_str(self):
        """Test the ingredient string representation."""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Onion'
        )

        self.assertEqual(str(ingredient), ingredient.name)


class RecipeTests(TestCase):
    """ Test the recipe model. """
    def test_recipe_str(self):
        """Test the recipe string representation."""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)