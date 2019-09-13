from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField()
    year_options=[('FE','First Year'),('SE','Second Year'),('TE','Third Year'),('BE','Final Year')]
    year=models.CharField(choices=year_options,max_length=2,default='FE')
    div =models.CharField(choices=[('A','A'),('B','B')],max_length=1,default='A')
    branch_options=[('Comps','Computers'),('IT','IT'),('EXTC','EXTC'),('Instru','Instru'),('Mech','Mechanical')]
    branch=models.CharField(choices=branch_options,max_length=10,default='Comps')
    rollno=models.IntegerField()

    def __str__(self):
        return self.user.username
