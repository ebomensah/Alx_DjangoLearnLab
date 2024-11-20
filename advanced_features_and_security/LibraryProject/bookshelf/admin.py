from django.contrib import admin
from .models import CustomUser, UserProfile
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_of_birth')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo' )}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    search_fields = ['user_username']

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.site_header = "User Administrator"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcome to User Administrator"

# Register your models here.

# Register your models here.
