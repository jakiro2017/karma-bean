from django.urls import path
from . import task_summary

urlpatterns = [
    path("", task_summary.task_summary, name="task_summary"),
    path("update_task", task_summary.update_task, name="update_task"),
]
