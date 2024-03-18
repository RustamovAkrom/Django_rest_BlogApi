from rest_framework import serializers 
from Api.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "bio", "birthday")