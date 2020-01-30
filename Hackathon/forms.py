from django import forms
from Hackathon.models import *
from django.contrib.auth.models import User


class register_form(forms.ModelForm):
    class Meta:
        model = team
        exclude = ['size']

