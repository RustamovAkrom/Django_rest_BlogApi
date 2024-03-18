from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from Api.models import User, Comment, Post, Like
from .services import request_user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "birthday", "bio")

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        birthday = validated_data['birthday']
        bio = validated_data['bio']
        user = User.objects.create(
            username = username,
            birthday = birthday,
            bio = bio,
        )
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "birthday", "bio")


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors")


class CommentSerializer(ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        read_only = True,
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = ("body", "authors", "posts")


class CommentListSerializer(ModelSerializer):
    authors = UserSerializer()
    posts = PostSerializer()

    class Meta:
        model = Comment
        fields = ("body", "authors", "posts")


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ("authors", "posts")


class PostDetailSerializer(ModelSerializer):
    authors = UserSerializer()
    comments = CommentListSerializer(many = True)
    likes = LikeSerializer(many = True)

    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors", "comments", "likes")


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors")


class MinAuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class MinPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title")


class LikeListSerializer(ModelSerializer):
    authors = MinAuthorSerializer()
    posts = MinPostSerializer()

    class Meta:
        model = Like
        fields = ("authors", "posts")


class TopPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors", "likes")