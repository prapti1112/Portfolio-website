from django.contrib import admin

from blogs.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "publish_date", "in_progress"]

admin.site.register(Blog, BlogAdmin)