# serializers.py
from rest_framework import serializers
from .models import Task,SpendPoint

class TaskSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='code.code', max_length=100)
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        s_type = validated_data["code"]["code"]
        spendpoint = SpendPoint.objects.get(code=s_type)
        # spendpoint_instance = SpendPoint.objects.create(**spendpoint_data)
        validated_data.pop("code")
        task_instance = Task.objects.create(code=spendpoint, **validated_data)
        return task_instance