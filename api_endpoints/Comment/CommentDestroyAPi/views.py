from .serializers import CommentDestroySerializer
from rest_framework.generics import DestroyAPIView
from Api.models import Comment
from .serializers import CommentDestroySerializer


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer

__all__ = ("CommentDestroyAPIView", )