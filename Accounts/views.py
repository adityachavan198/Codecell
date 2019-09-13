from django.shortcuts import render

# Create your views here.

def home(request):
    ''' The first page user visits '''
    return render(request,'Accounts/home.html',{}) 
