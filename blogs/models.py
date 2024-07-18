from django.db import models
from django.utils.timezone import now
from portfolio.models import Category
from django_editorjs import EditorJsField

class Blog(models.Model):
    """Model for Blogs.

    Args:
        models (django.model): .
    """
    title = models.CharField(blank=False, max_length=50, default="")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True )
    publish_date = models.DateField(default=now)
    # read_time = ""
    in_progress = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="uploads/blogs", default="https://dummyimage.com/450x300/dee2e6/6c757d.jpg")
    contents = EditorJsField(name="contents", editorjs_config={
            "tools":{
                "Link":{
                    "config":{
                        "endpoint": 'http://127.0.0.1:8000/blogs/edit/linkUpload',
                        "additionalRequestHeaders": [{ "Content-Type": "multipart/form-data" }],
                        },
                },
                "Image":{
                    "config":{
                        "endpoints":{
                            "byFile":'http://127.0.0.1:8000/blogs/edit/imageUpload',
                            "byUrl":'http://127.0.0.1:8000/blogs/edit/imageUpload'
                        },
                        "method": "POST",
                       "additionalRequestHeaders": [{ "Content-Type": "multipart/form-data" }],
                    }
                },
                "Attaches":{
                    "config":{
                        "endpoint":'http://127.0.0.1:8000/blogs/edit/fileUpload'
                    },
                    "additionalRequestHeaders": [{ "Content-Type": "multipart/form-data" }],
                }
              }
            }
        )
    # keywords = ArrayField( 
    #     models.CharField(blank=True, max_length=50), 
    #     blank=True, null=True, help_text="Keywords that reflect the main concepts used in the project" )
    