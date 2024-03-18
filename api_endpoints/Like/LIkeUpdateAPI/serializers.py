from rest_framework import serializers
from Api.models import Like


class LikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('authors', "posts", "created_at")