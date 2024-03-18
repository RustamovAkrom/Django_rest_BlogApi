from rest_framework.generics import DestroyAPIView
from .serializers import PostDestroySerializer, Post


class PostDestroyAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDestroySerializer

__all__ = ("PostDestroyAPIView", )