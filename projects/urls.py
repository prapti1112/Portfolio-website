from django.urls import path
from .views import ProjectsListView

urlpatterns = [
    path("", ProjectsListView.as_view(), name="listview"),
]