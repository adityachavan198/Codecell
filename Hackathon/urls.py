from django.conf.urls import url
from django.urls import path,re_path
from Hackathon import views
from Hackathon.views import Codequestion

Hackathon_url_patterns = [
    path('question/', Codequestion.as_view() , name = "Question"),
    ]
