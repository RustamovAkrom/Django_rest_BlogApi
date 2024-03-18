from rest_framework import serializers 
from Api.models import Post, User

class MiniAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "bio", "birthday")


class PostRetriveSerializer(serializers.ModelSerializer):
    authors = MiniAuthorSerializer()
    
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors")