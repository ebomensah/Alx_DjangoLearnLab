from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']  # Expose fields you need
        read_only_fields = ['created_at', 'updated_at']  # These fields should not be modified

        def update(self, instance, validated_data):
            validated_data.pop('author', None)
            return super().update(instance, validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model().objects.all())  # Reference to username
    
    post = PostSerializer (read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


