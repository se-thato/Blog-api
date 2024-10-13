from rest_framework import serializers
from .models import BlogPost, User

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'author', 'content', 'published_date', 'category']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ['id','username', 'email', 'password']