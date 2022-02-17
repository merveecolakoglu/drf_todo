from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import *

from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView

from api.models import Task
from api.serializers import TaskSerializer


@api_view(['GET'])
def apiOwerview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)


class TaskListView(ListAPIView):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer


class TaskDetailView(RetrieveAPIView):
    queryset = Task
    lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self, pk):
        queryset = Task.objects.get(id=pk)
        serializer = TaskSerializer(queryset, many=False)
        return Response(serializer.data)


class TaskUpdateView(UpdateAPIView):
    queryset=Task.objects.all()
    lookup_field = 'pk'
    serializer_class=TaskSerializer


class TaskDeleteView(DestroyAPIView):
    queryset=Task
    lookup_field = 'pk'

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

