from rest_framework import serializers
from Api.models import Comment, User, Post


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "authors", "posts")