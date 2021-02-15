from django.contrib import admin
from .models import Course, Instructor

class CourseAdmin(admin.ModelAdmin):

    list_display = ('name', )
    list_filter = ('name', )

class InstructorAdmin(admin.ModelAdmin):

    list_display = ('name', )
    list_filter = ('technology', )

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
