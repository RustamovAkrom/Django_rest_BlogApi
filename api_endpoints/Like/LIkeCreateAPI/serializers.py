from rest_framework import serializers
from Api.views import Like

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("authors", "posts", "created_at")