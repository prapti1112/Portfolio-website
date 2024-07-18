from django.contrib import admin

from .models import Experiment

class ExperimentAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "publish_date", "in_progress"]

admin.site.register(Experiment, ExperimentAdmin)