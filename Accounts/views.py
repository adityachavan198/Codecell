from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import View

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

class Register(View):
    User_form=UserForm
    Student_form=StudentForm
    template = 'Accounts/registration.html'

    def get(self, request, *args, **kwargs):
        ''' Process a get request '''
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        User_form = self.User_form()
        Student_form = self.Student_form()
        return render(request,self.template,{'user_form':User_form,'student_form':Student_form})

    def post(self, request, *args, **kwargs):
        ''' Process a post request '''
        User_form = self.User_form(request.POST)
        Student_form = self.Student_form(request.POST)

        if User_form.is_valid() and Student_form.is_valid():
            user = User_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            student=Student_form.save(commit=False)
            student.user=user
            student.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print(User_form.errors,Student_form.errors)
            return HttpResponseRedirect(reverse('home'))
    
def user_login(request, *args, **kwargs):
    ''' log in a user '''
    
    # if user is already logged in 
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    if request.method=='POST':
        try:
            next_page = request.GET['next']
        except:
            next_page = None

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                if next_page:
                    return HttpResponseRedirect(next_page)
                return HttpResponseRedirect(reverse('home'))
            else:
                print("Login failed")
                return HttpResponseRedirect(request,'Accounts/login.html',{})
        else:
            print("No such User")
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,'Accounts/login.html',{})