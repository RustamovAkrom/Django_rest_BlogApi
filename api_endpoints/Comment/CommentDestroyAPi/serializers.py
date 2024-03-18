from rest_framework import serializers
from Api.models import Comment

class CommentDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", "authors", "posts")