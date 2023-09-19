from django.contrib import admin
from .models import Task, SpendPoint


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin interface
    list_display = [
        "name",
        "deadline",
        "created_at",
        "updated_at",
        "code",
        "base_point",
        "base_point_predict",
        "base_point_penalty_if_fail",
        "note",
        "note_prediction",
    ]

    # Optionally, add filters and search fields
    list_filter = ["code"]
    search_fields = ["name"]


@admin.register(SpendPoint)
class SpendPointAdmin(admin.ModelAdmin):
    # Specify the fields to display in the admin interface
    list_display = ["name", "code", "explaination", "generic_demand", "isIncome"]

    # Optionally, add filters and search fields
    list_filter = ["code"]
