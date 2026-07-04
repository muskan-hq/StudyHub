from django.shortcuts import render

def home(request):
    context = {
        "name": "Muskan",
        "project":"StudyHub",
        "year":"Final year",
        "placement": False,
        "subjects": [
            "Python",
            "Django",
            "Computer Networks",
            "Machine Learning"
        ]
    }
    

    
    return render(request, "home/index.html",context,)