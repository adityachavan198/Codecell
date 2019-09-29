from django.conf.urls import url
from django.urls import path,re_path
from Forum import views

Forum_url_patterns = [

    path('', views.forum_home, name = "forum_home"),
    # path('Ask/',views, name = "Ask_question")
]
