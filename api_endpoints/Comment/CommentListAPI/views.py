from rest_framework.generics import ListAPIView
from Api.models import Comment
from .serialiers import CommentListSerializer

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

__all__ = ("CommentListAPIView",)
