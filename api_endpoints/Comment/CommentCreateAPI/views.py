from rest_framework.generics import CreateAPIView
from Api.models import Comment
from .serialiers import CommentCreateSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

__all__ = ("CommentCreateAPIView", )