from django.shortcuts import render, redirect
from .models import Task

def home(request):

    if request.method == "POST":
        task_name = request.POST["task_name"]

        if task_name:

            task = Task(
                task_name=request.POST["task_name"],
                time="1 hour",
                notes="Temporary Notes",
                score=0,
                submission=False
            )

            task.save()

    tasks = Task.objects.all()

    context = {
         "name": "Muskan",
        "project": "StudyHub",
        "year": "Final year",
        "placement": False,
        "tasks": tasks,
    }

    return render(request, "home/index.html", context)

def create_task(request):

    task = Task(
       task_name="Revise DBMS",
        time="2 Hours",
        notes="Complete revision before placement preparation",
        score=88,
        submission=True
    )

    task.save()

    return redirect("home")