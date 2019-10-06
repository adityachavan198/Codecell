from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
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

class Login_Register(View):
    template = 'Accounts/Login_Register.html'

    def get(self, request, *args, **kwargs):
        ''' Process a get request '''
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        return render(request,self.template,{})

    def post(self, request, *args, **kwargs):
        ''' Process a post request '''
        try:
            next_page = request.GET['next']
        except:
            next_page = None

        if request.POST.get('lusername'):
            username = request.POST.get('lusername')
            password = request.POST.get('lpassword')
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    if next_page:
                        return HttpResponseRedirect(next_page)
                    return HttpResponseRedirect(reverse('home'))
            else:
                return render(request , self.template, {'error':'There is an error in username or password, please try agian!'})
        elif request.POST.get('rusername'):
            username = request.POST.get('rusername')
            email = request.POST.get('remail')
            password = request.POST.get('rpassword')
            if username is not None and email is not None and password is not None:
                newuser = User.objects.create_user(username, email, password)
                newuser.set_password(password)
                newuser.save()
                student = Student.objects.create(user = newuser)
                student.save()
                if next_page:
                    return HttpResponseRedirect(next_page)
                return HttpResponseRedirect(reverse('home'))
            else:
                return render(request , self.template, {'error':'There is an error in your form, please try agian!'})
        
        return render(request , self.template, {'error':'There is an error, please try agian!'})

