from rest_framework.generics import UpdateAPIView
from .serializers import LikeUpdateSerializer, Like


class LikeUpdateAPIView(UpdateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeUpdateSerializer


__all__ = ("LikeUpdateAPIView", )