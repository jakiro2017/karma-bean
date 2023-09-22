from django.shortcuts import render
from django.utils import timezone
from ..models import Task


def task_summary(request):
    start_date = request.GET.get("start_date", timezone.now())
    end_date = request.GET.get("end_date", timezone.now())

    tasks = Task.objects.filter(created_at__range=[start_date, end_date])

    context = {
        "tasks": tasks,
        "start_date": start_date,
        "end_date": end_date,
    }

    return render(request, "karma_bean/tasks/ui/task_summary.html", context)
