from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.serializer import TaskSerializer
from tasks.models import Task

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(['GET'])
def task_list(request):
    """
    List all tasks.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data,status=200, safe=False)
