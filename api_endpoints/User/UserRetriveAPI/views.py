from rest_framework.generics import RetrieveAPIView
from .serializers import UserRetriveSerializer, User
from Api.debuger import debuger

class UserRetriveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetriveSerializer

    @debuger
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
__all__ = ("UserRetriveAPIView", )