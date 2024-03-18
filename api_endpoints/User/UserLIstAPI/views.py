from rest_framework.generics import ListAPIView
from .serializers import UserListSerializer, User
from Api.debuger import debuger


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    # @debuger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
__all__ = ("UserListAPIView", )