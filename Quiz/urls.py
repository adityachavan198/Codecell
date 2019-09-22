from django.conf.urls import url
from django.urls import path,re_path
from Quiz import views

Quiz_url_patterns = [

    path('', views.Categories_list_view.as_view(), name = 'quiz_category_list_all'),
    re_path(r'^(?P<category_name>[\w|W-]+)/$', views.View_Quizlist_by_Category.as_view(),name = 'Quiz_category_list_matching'),
]
