from rest_framework import serializers

from api.models import Task


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields ='__all__'