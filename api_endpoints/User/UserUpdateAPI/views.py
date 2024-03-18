from rest_framework.generics import UpdateAPIView
from .serializers import UserUpdateSerializer, User


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

__all__ = ("UserUpdateAPIView", )