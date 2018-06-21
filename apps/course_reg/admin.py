from __future__ import unicode_literals
from django.contrib import admin
from .models import Course, Description

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    ordering = ('name',)
    search_fields = ('name',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Description)
