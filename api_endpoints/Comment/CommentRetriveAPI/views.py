from rest_framework.generics import RetrieveAPIView
from .serializers import CommentRetriveSerializer, Comment


class CommentRetriveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetriveSerializer

__all__ = ("CommentRetriveAPIView", )