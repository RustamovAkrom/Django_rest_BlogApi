from rest_framework.generics import DestroyAPIView
from .serializers import UserDestroySerializer, User


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


__all__ = ("UserDestroyAPIView", )