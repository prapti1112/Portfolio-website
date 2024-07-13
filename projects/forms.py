from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [ "title", "description", "project_thumbnail", "demo", "code", "contents",  "in_progress", "category"]