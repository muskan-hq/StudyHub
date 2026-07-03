from django.shortcuts import render

def home(request):
    context = {
        "name": "Muskan",
        "project":"StudyHub",
        "year":"Final year"
    }
    return render(request, "home/index.html",context)