from rest_framework.generics import RetrieveAPIView
from .serializers import LikeRetriveSerializer, Like


class LikeRetriveAPIView(RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeRetriveSerializer

__all__ = ("LikeRetriveAPIView", )