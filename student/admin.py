from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):

    list_display = ('name', 'studentClass', )
    list_filter = ('name', 'studentClass', )

admin.site.register(Student, StudentAdmin)
