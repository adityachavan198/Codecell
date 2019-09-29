from django.conf.urls import url
from django.urls import path
from Accounts import views


registerpatterns = [
	path('register/',views.Register.as_view(),name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('login/',views.user_login,name='login'),
]