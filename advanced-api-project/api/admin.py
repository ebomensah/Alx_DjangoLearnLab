from django.contrib import admin
from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_year', 'author']
    search_fields = ['title', 'publication_year', 'author']

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Author, AuthorAdmin)


# Register your models here.
