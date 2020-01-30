from django import forms
from Accounts.models import *
from django.contrib.auth.models import User

class login_form(forms.Form):
    # password=forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    fields = ['username', 'password']

class user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class student_form(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['githublink', 'facebooklink', 'linkedinlink', 'instagramlink','user']