from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object."""

    class Meta:
        model = User
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it."""
        return User.objects.create_user(**validated_data)
