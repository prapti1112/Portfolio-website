import json
from venv import logger
from django.db.models.query import QuerySet
from django.views.generic import ListView
from portfolio.models import Category
from projects.models import Project
from .filters import ProjectFilter


with open("color_palette.json") as file:
    color_pallete = json.load(file)


class ProjectsListView(ListView):
    model = Project
    template_name = r"projects\project_card_view.html"
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["projects"] = Project.objects.all()
        # context["categories"] = Category.objects.all()
        context['form'] = self.filterset.form

        context = { **context, **color_pallete}

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProjectFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
