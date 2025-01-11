from django.db.models import ForeignKey
from .models import Book, Author, User, Comment, BlogPost
from rest_framework import serializers
from django.core.exceptions import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self,value):

        #Custom validation to check if the publication year is in the future.

        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):

      #Serializer for the Author model.
     #Includes the 'name' field and a nested list of books for the related books.

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['full_name', 'first_name', 'last_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at']


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)  # Nested serializer for comments

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'comments', 'likes']

    # Ensure that the comment author is the same as the blog post author
    def validate_comments(self, value):
        blog_post_author = self.initial_data.get('author')
        for comment_data in value:
            comment_author = comment_data.get('author')
            if comment_author != blog_post_author:
                raise ValidationError("The comment author must be the same as the blog post author.")
        return value

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])
        blog_post = BlogPost.objects.create(**validated_data)
        for comment_data in comments_data:
            comment_data['blog_post'] = blog_post  # Link the comment to the blog post
            Comment.objects.create(**comment_data)
        return blog_post

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments', [])
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()


     # Update comments
        for comment_data in comments_data:
            comment_id = comment_data.get('id')
            if comment_id:
                comment = Comment.objects.get(id=comment_id, blog_post=instance)
                comment.content = comment_data.get('content', comment.content)
                comment.save()
            else:
                comment_data['blog_post'] = instance
                Comment.objects.create(**comment_data)

        return instance