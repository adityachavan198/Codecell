from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Accounts.forms import *

# Create your views here.

def home(request):
    ''' The first page user visits '''
    return render(request,'Accounts/home.html',{}) 


@login_required
def user_logout(request):
    ''' Logout the user from his session'''
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    ''' Register a new user first if is user submits data and second is load a form '''
    registered=False

    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        student_form=StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            student=student_form.save(commit=False)
            student.user=user
            student.save()
            return HttpResponseRedirect(reverse('home'))

        else:
            print(user_form.errors,student_form.errors)
    else:
        user_form=UserForm()
        student_form=StudentForm()
    return render(request,'Accounts/registration.html',{'user_form':user_form,'student_form':student_form})

def user_login(request):
    ''' log in a user '''
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                print("Login failed")
                return HttpResponseRedirect(request,'Accounts/login.html',{})
        else:
            print("No such User")
            return HttpResponseRedirect('')
    else:
        return render(request,'Accounts/login.html',{})