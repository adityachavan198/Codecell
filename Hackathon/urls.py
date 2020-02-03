from django.conf.urls import url
from django.urls import path,re_path
from Hackathon import views

Hackathon_url_patterns = [
    path('', views.hackathon_home, name = 'hackathon_home'),
    path('register_page', views.hackathon_register, name = 'hackathon_register'),
    path('shedule', views.shedule , name = 'shedule'),
    path('problem_statements', views.ps, name = 'ps'),
    path('countdown', views.countdown , name = 'countdown'),
    path('faq', views.faq , name = 'faq'),
    path('sponsors', views.sponsors , name = 'sponsors'),
    path('paralax', views.paralax , name = 'paralax'),
    path('first', views.first , name = 'first'),
]