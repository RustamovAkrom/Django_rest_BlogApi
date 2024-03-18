from rest_framework import serializers 
from Api.models import Post


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", "authors")