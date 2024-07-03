"""Filter for search over all projects"""
from django import forms
import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
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

    # category = django_filters.ChoiceFilter(
    #     choices = "category",
    #     lookup_expr='exact',
    #     widget = forms.Select(
    #         attrs={
    #             "class":"btn btn-secondary dropdown-toggle",
    #             "aria-labelledby":"dropdownMenuButton",
    #         }
    #     )
    # )


    class Meta:
        model = Project
        # fields = {
        #     'title': [ 'icontains' ],
        #     'category': [ 'exact' ],
        # }
        fields = [ 'title', 'category' ]