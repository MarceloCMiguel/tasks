import re
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from tasks.serializer import TaskSerializer
from tasks.models import Task
import django
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(['GET'])
def task_list(request):
    """
    List all tasks.
    """
    django.middleware.csrf.get_token(request)
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        #print(serializer.data)
        return HttpResponse(JsonResponse( serializer.data,safe=False))
    if request.method == 'POST':
        return render(request,'forms.html')


def post_task(request):
    """
    Post a new task.
    """  
    if request.method == "POST":  
        form = TaskSerializer(data=request.POST)
        print("foi post")
        if form.is_valid():  
            try:  
                form.save()  
                print("deu certo")
                return HttpResponse(JsonResponse({'data':'ok'},safe=False))
            except Exception as e: 
                return HttpResponse(JsonResponse({'data':e},safe=False))
        else:
            return HttpResponse(JsonResponse({'data':'error'},safe=False))
    else:
        return render(request,'forms.html')

def delete_task(request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return HttpResponse(JsonResponse({'data':'ok'},safe=False))
