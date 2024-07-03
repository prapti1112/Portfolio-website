from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "last_modified", "in_progress", "category"]

admin.site.register(Project, ProjectAdmin)