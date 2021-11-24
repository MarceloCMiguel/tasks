import re
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
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
    if request.method == 'POST':
        return render(request,'forms.html')


def post_task(request):  
    if request.method == "POST":  
        form = TaskSerializer(data=request.POST)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/tasks/get_tasks')  
            except Exception as e:  
                print(e) 
    return render(request,'forms.html')

