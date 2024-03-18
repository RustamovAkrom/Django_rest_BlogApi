from rest_framework.generics import RetrieveAPIView
from .serializers import PostRetriveSerializer, Post
from Api.permisions import IsOwner

class PostRetriveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetriveSerializer
    permission_classes = [IsOwner, ]
__all__ = ("PostRetriveAPIView", )