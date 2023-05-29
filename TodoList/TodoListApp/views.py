from django.shortcuts import render
from django.views import View
from .models import Task


class TaskList(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'TodoListApp/task_list.html', context=context)


class TaskDetail(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        context = {
            'task': task
        }
        return render(request, 'TodoListApp/task_detail.html', context=context)
