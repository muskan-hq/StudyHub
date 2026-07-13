from django.shortcuts import render
from .models import Task
def home(request):
    tasks = Task.objects.exclude(task_name="Django")
    context = {
        "name": "Muskan",
        "project":"StudyHub",
        "year":"Final year",
        "placement": False,
        "tasks":tasks,
    
    }
   

    
    return render(request, "home/index.html",context,)