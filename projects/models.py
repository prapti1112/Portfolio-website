import uuid
from django.utils.timezone import now
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from portfolio.models import Category
from django_editorjs import EditorJsField

class Project(models.Model):
    """Model for Projects.

    Args:
        models (django.model): .
    """
    title = models.CharField(blank=False, max_length=50, default="")
    short_description = models.CharField(name="short_description", max_length=60, default="Short description about the project")
    description = models.TextField(name="description",  max_length=500, blank=False, null=True)
    project_thumbnail = models.ImageField(upload_to="uploads/projects", default="https://dummyimage.com/450x300/dee2e6/6c757d.jpg")
    demo_link = models.URLField(name="demo", null=True, default="https://github.com/prapti1112/")
    code_link = models.URLField(name="code", null=True, default="https://github.com/prapti1112/")
    # contents = models.TextField(name="contents", default = "Contents of the project")
    contents = EditorJsField(name="contents")
    last_modified = models.DateField(default=now)
    in_progress = models.BooleanField(default=False)
    # keywords = ArrayField( 
    #     models.CharField(blank=True, max_length=50), 
    #     blank=True, null=True, help_text="Keywords that reflect the main concepts used in the project" )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True )
