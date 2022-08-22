from rest_framework import viewsets, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from user.serializers import UserSerializer, AuthTokenSerializer
from user.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """
        user 정보 리턴 api
    """
    def list(self, reqeuest, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in th system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    # renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    # cookie, Token 등
    authentication_classes = (authentication.TokenAuthentication, )
    # 등록된 유저만 접근가능 하도록 permission 체크
    permission_classes = (permissions.IsAuthenticated, )

    # retrieve and return authenticated user
    # this method is also required for update (patch)
    def get_object(self):
        """Retrieve and return authentication user."""
        return self.request.user
