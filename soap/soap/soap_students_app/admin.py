from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission', 'full_name', 'email', 'phone_number', 'address', 'entry_points', 'reg_date')
    list_filter = ['reg_date']
    search_fields = ['full_name']

admin.site.register(Student, StudentAdmin)