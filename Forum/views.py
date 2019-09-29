from django.shortcuts import render
from Forum.models import *
# Create your views here.

def forum_home(request, *args, **kwargs):
    question_list = Forum_question.objects.all().order_by('-asked_on')
    print(question_list)
    return render(request,'Forum/Forum_home.html',{'question_list':question_list})

# class Ask_question(View):
