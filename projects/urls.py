from django.urls import path
from .views import ProjectsListView, ProjectDetailView, editProject, upload_file, upload_image, upload_link_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", ProjectsListView.as_view(), name="list_view"),
    path("<int:pk>", ProjectDetailView.as_view(), name="detail_view"),
    path("<int:pk>/edit", editProject, name="edit"),
    path("edit/fileUpload", csrf_exempt(upload_file), name="file_upload"),
    path("edit/imageUpload", csrf_exempt(upload_image), name="image_upload"),
    path("edit/linkUpload", csrf_exempt(upload_link_view), name="link_upload"),
]