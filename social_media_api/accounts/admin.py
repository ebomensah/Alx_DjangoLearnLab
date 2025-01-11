from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'profile_picture']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
