from django.contrib import admin
from django.contrib.auth.models import User
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'author']

admin.site.register(Book, BookAdmin)
# Register your models here.
