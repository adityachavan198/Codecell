from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.db import IntegrityError
from django.views.decorators.clickjacking import xframe_options_exempt

from Accounts.forms import *

from Accounts.forms import *

# Create your views here.

def home(request):
    ''' The first page user visits '''
    template = 'Accounts/home.html'
    if request.method == 'GET':
        return render(request,'Accounts/home.html',{})


@login_required
def user_logout(request):
    ''' Logout the user from his session'''
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def student_login(request):
    template = 'Accounts/login.html'
    try:
        next_page = request.GET['next']
    except:
        next_page = None

    if request.method == "POST":
        form = login_form(request.POST)
        print("hi")
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next_page:
                        return HttpResponseRedirect(next_page)
                    return HttpResponseRedirect(reverse('home'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        form = login_form()
    return render(request, template, {'form': form})

def register(request):
    template = 'Accounts/register.html'
    if request.method == "POST":
        form1 = user_form(request.POST)
        form2 = student_form(request.POST)
        print("A")
        if form1.is_valid() and form2.is_valid():
            print("B")
            user = form1.save()
            user.set_password(user.password)
            user.save()
            student = form2.save(commit=False)
            student.user = user
            student.save()
            return HttpResponseRedirect(reverse('authenticate'))
    else:
        form1 = user_form()
        form2 = student_form()
    return render(request, template, {'form1': form1,'form2':form2})

@xframe_options_exempt
def team(request):
    return render(request, 'Accounts/team.html',{})

class User_profile(View):
    template_name = "Accounts/profile.html"

    def get(self, request, *args, **kwargs):
        if request.user.student.paid == False:
            return HttpResponseRedirect(reverse('payment'))
        user = get_object_or_404(User, username = kwargs['username'])
        student = get_object_or_404(Student, user = user)
        can_edit = False
        if request.user.is_authenticated and request.user == user:
            can_edit = True
        return render(request, self.template_name, {"user":user,"student":student,"can_edit":can_edit})

class User_update(View):
    template_name = "Accounts/profile_update.html"

    def get(self, request, *args, **kwargs):
        if request.user.student.paid == False:
            return HttpResponseRedirect(reverse('payment'))
        user = get_object_or_404(User, username = kwargs['username'])
        student = get_object_or_404(Student, user = user)
        if request.user.is_authenticated and request.user == user:
            return render(request, self.template_name, {})
        else:
            return HttpResponseRedirect(reverse('home'))    
        
        


    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username = kwargs['username'])
        student = get_object_or_404(Student, user = user)
        if request.user.is_authenticated and request.user == user:

            Form = request.POST
            print(Form)
            if Form['first_name']=="" or Form['last_name']=="" or Form['birthday']=="" or Form["email"]=="" or Form["phone"]=="":
                error = "There is an error in your form"
                return render(request, self.template_name, {"error":error})
            else:
                user.first_name = Form['first_name']
                user.last_name = Form['last_name']
                user.email = Form['email']
                student.description = Form['description']
                student.birthdate = str(Form['birthday'])
                student.gender = Form['gender']
                student.stream = Form['stream']
                student.phone = Form['phone']
                student.githublink = Form['github']
                student.facebooklink = Form['facebook']
                student.linkedinlink = Form['linkedin']
                student.instagramlink = Form['instagram']
                student.achname1 = Form['achname1']
                student.ach1 = Form['achievement1']
                student.achname2 = Form['achname2']
                student.ach2 = Form['achievement2']
                student.achname3 = Form['achname3']
                student.ach3 = Form['achievement3']
                student.achname4 = Form['achname4']
                student.ach4 = Form['achievement4']

                user.save()
                student.save()

                return HttpResponseRedirect(reverse('home'))

        return HttpResponseRedirect(reverse('home'))

def payment(request):
    return render(request, 'Accounts/payment.html', {})