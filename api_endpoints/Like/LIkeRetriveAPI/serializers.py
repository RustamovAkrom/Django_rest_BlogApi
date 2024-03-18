from rest_framework import serializers
from Api.models import Like, Post, User

class MiniAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("bio")


class MiniPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active",  "created_at")


class LikeRetriveSerializer(serializers.ModelSerializer):
    # posts = MiniPostSerializer()

    class Meta:
        model = Like
        fields = ("authors", "posts", "created_at")

        