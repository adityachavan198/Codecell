from django.conf.urls import url
from django.urls import path,re_path
from Accounts import views

registerpatterns = [
    path('logout/',views.user_logout,name='logout'),
    path('login/', views.student_login, name = "authenticate"),
    path('register/',views.register, name = "register"),
    path('payment/', views.payment, name = "payment")
    
]