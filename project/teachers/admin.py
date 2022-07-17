from django.contrib import admin
from .models import *

# Register your models here.

class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name']

admin.site.register(Teachers,TeachersAdmin)
