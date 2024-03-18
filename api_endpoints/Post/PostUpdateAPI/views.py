from rest_framework.generics import UpdateAPIView
from .serializers import PostUpdateSerializer, Post


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

__all__ = ("PostUpdateAPIView", )