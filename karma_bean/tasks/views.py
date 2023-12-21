# views.py
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .ser import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
@method_decorator(csrf_exempt, name='dispatch')
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        # Assuming request.data is a list of dictionaries with Task data
        tasks_data = request.data
        for i in tasks_data:
            i['base_point'] = int(i['pointNeed'])
            i.pop('pointNeed')
        serializer = TaskSerializer(data=tasks_data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
