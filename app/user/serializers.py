from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

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
class AuthTokenSerializer(serializers.Serializer):
    """Serializer for user authentication object."""
    # create fields to get data for authentication
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
        min_length=5
    )

    # override validate method and raise exception if invalid
    def validate(self, attrs):
        # attrs contains all the serializer fields defined above
        email = attrs.get('email')
        password = attrs.get('password')

        # authenticate -> username 기준으로 인증시스템 구축
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            # we use gettext to enable language translation for this text
            msg = _('Unable to authenticate with credentials provided')
            # pass correct code will raise the relevant http status code
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
