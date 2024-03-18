from rest_framework import serializers
from Api.models import Comment, User

class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "bio")

class CommentRetriveSerializer(serializers.ModelSerializer):
    authors = MiniUserSerializer()
    class Meta:
        model = Comment
        fields = ("body", "authors", "posts")
