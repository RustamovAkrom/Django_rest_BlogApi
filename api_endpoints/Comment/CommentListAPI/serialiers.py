from rest_framework import serializers
from Api.models import Comment, User, Post


class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "birthday", "bio")


class MiniPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors")


class CommentListSerializer(serializers.ModelSerializer):
    # authors = MiniUserSerializer(many=True)
    # posts = MiniPostSerializer(many=True)
    
    class Meta:
        model = Comment
        fields = ("body", "authors", "posts")