from django.urls import path
from .views import ProjectsListView, ProjectDetailView

urlpatterns = [
    path("", ProjectsListView.as_view(), name="list_view"),
    path("<int:pk>", ProjectDetailView.as_view(), name="detail_view"),
]