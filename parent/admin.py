from django.contrib import admin
from .models import Parent

class ParentAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(Parent, ParentAdmin)

