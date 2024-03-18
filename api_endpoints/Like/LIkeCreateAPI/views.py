from rest_framework.generics import CreateAPIView
from .serializers import LikeCreateSerializer, Like

class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeCreateSerializer
    
__all__ = ("LikeCreateAPIView", )