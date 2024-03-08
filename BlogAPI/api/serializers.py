from rest_framework import serializers
from .models import Post
from accounts.models import CustomUser


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title','body','created_at']

class UserSerializer(serializers.ModelSerializer): 
    model = CustomUser
    fields = ["id", "username"]
