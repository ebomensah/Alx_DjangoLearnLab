from django.contrib import admin
from .models import User, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    search_fields = ['user_username']

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.site_header = "User Administrator"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcome to User Administrator"

# Register your models here.

# Register your models here.
