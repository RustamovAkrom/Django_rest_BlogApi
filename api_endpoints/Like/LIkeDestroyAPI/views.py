from rest_framework.generics import DestroyAPIView
from .serializers import LikeDestroySerializer, Like


class LikeDestroyAPIView(DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeDestroySerializer
    
__all__ = ("LikeDestroyAPIView", )