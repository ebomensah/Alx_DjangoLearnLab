from django.contrib import admin
from .models import Profile, Post, Comment

class ProfileAdmin(admin.ModelAdmin):
    list_fields = ['username', 'email']
    search_fields = ['username', 'email']
admin.site.register(Profile, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_fields = ['title', 'content', 'published_date', 'author']
    search_fields = ['author', 'title']
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_fields = ['post', 'content', 'created_at']
    search_fields = ['created_at', 'post']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
