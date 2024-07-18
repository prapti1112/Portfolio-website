from django.forms import ModelForm
from .models import Experiment

class ProjectForm(ModelForm):
    class Meta:
        model = Experiment
        fields = [ "title", "contents", "publish_date", "in_progress", "category"]