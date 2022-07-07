from django.contrib import admin
from .models import *

# Register your models here.


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    list_filter = ['available']
    search_fields = ['name']

admin.site.register(Courses,CoursesAdmin)
