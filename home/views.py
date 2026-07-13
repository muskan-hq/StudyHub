from django.shortcuts import render
from .models import Task
def home(request):
    tasks = Task.objects.filter(score__gte=80)
    context = {
        "name": "Muskan",
        "project":"StudyHub",
        "year":"Final year",
        "placement": False,
        "tasks":tasks,
    
    }
   

    
    return render(request, "home/index.html",context,)