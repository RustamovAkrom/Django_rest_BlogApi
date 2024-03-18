from rest_framework.generics import ListAPIView
from .serializers import PostListSerializer, Post
from Api.debuger import debuger

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all() #.prefetch_related("comments", "authors") #.select_related("authors")
    serializer_class = PostListSerializer

    @debuger
    def get_queryset(self):
        return super().get_queryset()
    
__all__ = ("PostListAPIView", )