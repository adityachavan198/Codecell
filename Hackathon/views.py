import os
from django.shortcuts import render
from django.views import View

def hackathon_home(request, *args, **kwargs):
    return render(request, "Hackathon/hackathon_home.html", {})