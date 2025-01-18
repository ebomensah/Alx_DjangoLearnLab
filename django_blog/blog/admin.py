from django.contrib import admin
from .models import Profile, Post

class ProfileAdmin(admin.ModelAdmin):
    list_fields = ['username', 'email']
    search_fields = ['username', 'email']
admin.site.register(Profile, ProfileAdmin)

class PostAdmin(admin.ModelAdmin):
    list_fields = ['title', 'content', 'published_date', 'author']
    search_fields = ['author', 'title']
admin.site.register(Post, PostAdmin)

# Register your models here.
