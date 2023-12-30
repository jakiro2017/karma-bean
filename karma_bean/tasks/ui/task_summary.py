from django.shortcuts import render
from django.utils import timezone
from ..models import Task, SpendPoint,TaskStatus
from django.http import JsonResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt

field_map = {
    "0": "id",
    "1": "name",
    "2": "state",
    "3": "code",
    "4": "base_point",
    # "4": "base_point",
    "6": "note",
    "7": "deadline",
}


def task_summary(request):
    start_date = request.GET.get("start_date", timezone.now())
    end_date = request.GET.get("end_date", timezone.now())
    status = request.GET.get("status", None)

    tasks = Task.objects.filter(created_at__range=[start_date, end_date])

    # Check if status is provided and not an empty string
    if status and status.strip():
        tasks = tasks.filter(status=status)

    spendpoints = SpendPoint.objects.all()
    context = {
        "tasks": tasks,
        "start_date": start_date,
        "end_date": end_date,
        "spendpoints": spendpoints,
        'TaskStatus': TaskStatus
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

@csrf_exempt
def update_task_stat(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        new_stat = request.POST.get("new_stat")

        # Get the Task and SpendPoint instances
        task = Task.objects.get(id=task_id)
        

        # Update the Task instance
        try:
            task.status = new_stat
            task.save()
        except Exception as e:
            return HttpResponseServerError(e.args[0])

        return JsonResponse({"status": "success"})