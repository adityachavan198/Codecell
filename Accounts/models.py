from django.db import models
from django.contrib.auth.models import User
from Forum.models import *

# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    year_options=[('FE','First Year'),('SE','Second Year'),('TE','Third Year'),('BE','Final Year')]
    year=models.CharField(choices=year_options, max_length=2, default='SE')
    div =models.CharField(choices=[(i,i) for i in "ABCDEFG"], max_length=1, default='A')
    branch_options=[('Comps','Computers'),('IT','IT'),('EXTC','EXTC'),('Instru','Instru'),('Mech','Mechanical')]
    branch=models.CharField(choices=branch_options, max_length=10, default='Comps')
    rollno=models.IntegerField(blank = False, null = False, default = 1)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name="Student"
        verbose_name_plural="Students"



# Monkey Patching
def doubts_asked(self):
    return Forum_question.objects.all().filter(user = self).count()

def doubts_solved(self):
    return Forum_answer.objects.all().filter(user = self).count()

def total_users(self):
    return User.objects.all().count()

User.add_to_class("doubts_asked",doubts_asked)
User.add_to_class("doubts_solved",doubts_solved)
User.add_to_class("total_users", total_users)