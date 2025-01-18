from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'content', 'created_at', 'updated_at']
    fields = ['author', 'title', 'content']

    class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'created_at')
        fields = ('title', 'content', 'author')

        def save_model(self, request, obj, form, change):
            if not obj.author:
                obj.author = request.user
            super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_at', 'updated_at']
    fields= ['author','post', 'content']
    
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Comment, CommentAdmin)

# Register your models here.
