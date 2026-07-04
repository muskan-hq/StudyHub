from django.shortcuts import render

def home(request):
    context = {
        "name": "Muskan",
        "project":"StudyHub",
        "year":"Final year",
        "placement": False,
        "subjects": [
            "HTML",
            "JavaScript",
            "Django",
            "Database",
            
        ]
    }
    

    
    return render(request, "home/index.html",context,)