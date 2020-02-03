from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.clickjacking import xframe_options_exempt

from Hackathon.models import *
from Hackathon.forms import *

def hackathon_home(request, *args, **kwargs):
    return render(request, "Hackathon/hackathon_home.html", {})

def hackathon_register(request):
    template = 'Hackathon/index.html'

    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            team = form.save(commit = False)
            if team.mate3_name and team.mate4_name:
                team.size = 4
            elif team.mate3_name:
                team.size = 3
            else:
                team.size = 2
            team.save()
            return redirect('hackathon_home')
    else:
        form = register_form()
    return render(request, template, {'form': form})

def ps(request):
    return render(request, "Hackathon/ps.html", {})

@xframe_options_exempt
def shedule(request):
    return render(request, "Hackathon/shedule1.html",{})

@xframe_options_exempt
def countdown(request):
    return render(request, "Hackathon/countdown.html",{})

@xframe_options_exempt
def faq(request):
    return render(request, "Hackathon/faq.html",{})

@xframe_options_exempt
def sponsors(request):
    return render(request, "Hackathon/sponsors.html",{})

@xframe_options_exempt
def paralax(request):
    return render(request, "Hackathon/paralax.html",{})

@xframe_options_exempt
def first(request):
    return render(request, "Hackathon/first.html",{})
