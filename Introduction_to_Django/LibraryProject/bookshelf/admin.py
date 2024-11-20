from django.contrib import admin
from .models import Book
from .models import Department
from .models import Employee

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','clearance')
    search_fields= ('name', 'clearance')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name', 'department')
    search_fields=('name', 'department')


admin.site.register(Book, BookAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)

admin.site.site_header = "Bookshelf Administrator"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Welcome to Bookshelf"

# Register your models here.