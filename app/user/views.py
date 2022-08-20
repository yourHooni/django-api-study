from rest_framework import viewsets
from rest_framework.response import Response

from user.serializers import UserSerializer
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

    def create(self, request, *args, **kwargs):
        pass
