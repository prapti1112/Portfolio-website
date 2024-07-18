"""Filter for search over all blogs"""
from django import forms
import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        # field_name='title',
        lookup_expr='icontains',
        label="",
        widget=forms.TextInput(
            attrs={
            "class":"col form-control mr-sm-2",
            "type":"search",
            "placeholder": "Search",
            "aria-label": "Search",
            }
        )
    )


    class Meta:
        model = Blog
        fields = [ 'title', 'category' ]