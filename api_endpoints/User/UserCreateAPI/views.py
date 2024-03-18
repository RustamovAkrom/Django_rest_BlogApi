from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializers, User


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers

__all__ = ("UserCreateAPIView", )