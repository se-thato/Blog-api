from rest_framework import serializers
from .models import Post, User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'published_date', 'category']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ['id','username', 'email', 'password']