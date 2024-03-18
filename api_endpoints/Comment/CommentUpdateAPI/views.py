from rest_framework.generics import UpdateAPIView
from .serializers import CommentUpdateSerializer, Comment


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer

__all__ = ("CommentUpdateAPIView", )