import os
from django.shortcuts import render
from django.views import View
from Hackathon.models import *

def hackathon_home(request, *args, **kwargs):
    return render(request, "Hackathon/hackathon_home.html", {})

def hackathon_register(request):
    problems_db = problems.objects.all()
    problems_var=dict()
    for i in problems_db:
        problems_var[i.id]={"title":i.title,"statement":i.statement,"category":i.Category}
    print("\n\n\n\nnsgasfg\n\n\n\n",problems_var)

    return render(request,"Hackathon/hackathon_register.html",{'problems':problems_var})
