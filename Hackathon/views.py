import os
from django.shortcuts import render, redirect
from django.views import View
from Hackathon.models import *
from Hackathon.forms import *

def hackathon_home(request, *args, **kwargs):
    return render(request, "Hackathon/hackathon_home.html", {})

def hackathon_register(request):
    template = 'Hackathon/hackathon_register1.html'

    if request.method == "POST":
        form = register_form(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('hackathon_home')
    else:
        form = register_form()
    return render(request, template, {'form': form})

