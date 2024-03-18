from rest_framework.generics import CreateAPIView
from .serializers import PostCreateSerializer, Post


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

__all__ = ("PostCreateAPIView", )