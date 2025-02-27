from django.urls import path
from django.contrib import admin
from tasks.views import TaskListView, TaskDetailView, TaskCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
]
