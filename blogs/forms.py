from django.forms import ModelForm
from .models import Blog

class ProjectForm(ModelForm):
    class Meta:
        model = Blog
        fields = [ "title", "contents", "publish_date", "in_progress", "category"]