from django.shortcuts import render
from django.utils import timezone
from ..models import Task, SpendPoint
from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

field_map = {
    "0": "id",
    "1": "name",
    "2": "code",
    # "3": "created_at",
    "3": "base_point",
    "4": "base_point",
    "6": "deadline",
}


def task_summary(request):
    start_date = request.GET.get("start_date", timezone.now())
    end_date = request.GET.get("end_date", timezone.now())

    tasks = Task.objects.filter(created_at__range=[start_date, end_date])
    spendpoints = SpendPoint.objects.all()
    context = {
        "tasks": tasks,
        "start_date": start_date,
        "end_date": end_date,
        "spendpoints": spendpoints,
    }

    return render(request, "karma_bean/tasks/ui/task_summary.html", context)


@csrf_exempt
def update_task(request):
    if request.method == "POST":
        id = request.POST.get("id")
        field = request.POST.get("columnIndex")
        field = field_map[field]
        new_content = request.POST.get("new_content")
        try:
            task = Task.objects.get(id=id)
            setattr(task, field, new_content)
            task.save()
        except Exception as e:
            return HttpResponseServerError(e.args[0])

    return JsonResponse({"status": "success"})


@csrf_exempt
def update_task_code(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        new_code = request.POST.get("new_code")

        # Get the Task and SpendPoint instances
        task = Task.objects.get(id=task_id)
        spendpoint = SpendPoint.objects.get(code=new_code)

        # Update the Task instance
        try:
            task.code = spendpoint
            task.save()
        except Exception as e:
            return HttpResponseServerError(e.args[0])

        return JsonResponse({"status": "success"})
