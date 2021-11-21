from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_tasks', views.task_list, name='get_tasks'),

]
