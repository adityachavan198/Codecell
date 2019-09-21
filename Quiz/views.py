from django.shortcuts import render
from django.views.generic import ListView
from Quiz.models import *

# Create your views here.

class Categories_list_view(ListView):
    model = Category
