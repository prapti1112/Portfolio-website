from django.contrib import admin
from .models import Skill, Category, WorkExperience


class SkillAdmin(admin.ModelAdmin):
    list_display = ["skill", "skill_level", "work_experience"]

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ["company_name", "role"]

admin.site.register(Category)
admin.site.register(Skill, SkillAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)