from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'content', 'created_at', 'updated_at']
    search_fields = ['author', 'title', 'created_at']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_at', 'updated_at']
    search_fields= ['author', 'created_at']

admin.site.register(Comment, CommentAdmin)

# Register your models here.
