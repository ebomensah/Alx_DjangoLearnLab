from django.contrib import admin
from .models import Book, Author, User, BlogPost

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'author']
    search_fields = ['title', 'publication_year', 'author']

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields= ['first_name', 'last_name']

admin.site.register(User, UserAdmin)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content',  'created_at']
    search_fields = ['title', 'author', 'content', 'created_at']

admin.site.register (BlogPost, BlogPostAdmin)

# Register your models here.
