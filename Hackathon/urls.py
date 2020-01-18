from django.conf.urls import url
from django.urls import path,re_path
from Hackathon import views

Hackathon_url_patterns = [
    path('', views.hackathon_home, name = 'hackathon_home'),
]