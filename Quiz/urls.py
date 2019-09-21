from django.conf.urls import url
from django.urls import path
from Quiz import views

Quiz_url_patterns = [

    path('', views.Categories_list_view.as_view(), name = 'quiz_category_list_all'),
]
