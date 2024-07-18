from django.contrib import admin

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "publish_date", "in_progress"]

admin.site.register(Blog, BlogAdmin)