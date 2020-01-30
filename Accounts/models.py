from django.db import models
from django.contrib.auth.models import User
from Forum.models import *
from django.core.validators import RegexValidator

# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    branch=models.CharField(max_length=10, default='Computer', verbose_name="Branch")

    description=models.CharField(max_length=100, blank = True,help_text="Description about yourself")

    college_name = models.CharField(max_length=100, blank = True, verbose_name="College Name")

    birthdate = models.DateTimeField()

    gender = models.CharField(max_length = 50, choices = (("Male","Male"),("Female","Female")))

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex], max_length=14, blank=True)

    githublink = models.CharField(max_length = 70, blank = True, default = "")

    facebooklink = models.CharField(max_length = 70, blank = True, default = "")

    instagramlink = models.CharField(max_length = 70, blank = True, default = "")

    linkedinlink = models.CharField(max_length = 70, blank = True, default = "")

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