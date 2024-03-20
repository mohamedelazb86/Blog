from rest_framework import serializers
from .models import Post

class PostListSerializers(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'
class Post_DetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'