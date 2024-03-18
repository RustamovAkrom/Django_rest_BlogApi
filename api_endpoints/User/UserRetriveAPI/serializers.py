from rest_framework import serializers 
from Api.models import User, Comment, Post

class MiniCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("body", )

    
class MiniPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "is_active", )


class UserRetriveSerializer(serializers.ModelSerializer):
    posts = MiniPostSerializer(many = True)
    comments = MiniCommentSerializer(many = True)
    
    class Meta:
        model = User
        fields = ("username", "bio", "birthday", "comments", "posts")