from rest_framework.generics import ListAPIView
from .serializers import LikeListSerializer, Like


class LikeListAPIView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer

__all__ = ("LikeListAPIView", )