from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator

# Create your models here.

categories = (
    ('Machine Learning','Machine Learning'),
    ('IOT','IOT'),
    ('Web Development','Web Development'),
    ('App Developement', 'App Development'),
)

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")

class problems(models.Model):

    title = models.CharField(verbose_name= "Title", max_length = 50, blank = False)

    statement = models.CharField(verbose_name = "Problem Statement", max_length = 500, blank = False)

    Category = models.CharField(verbose_name="Category", max_length=30, default='Machine Learning',
                             choices=categories)

    def __str__(self):
        return self.title

class team(models.Model):

    name = models.CharField(verbose_name = "Team Name", max_length= 50, blank= False)

    size = models.PositiveSmallIntegerField(blank = False, default = 4, verbose_name = "Team Size", help_text = "No. of player in a team", validators = [MaxValueValidator(4)] )

    leader_name = models.CharField(verbose_name = "Team Leader name", max_length= 50, blank= False)

    leader_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)

    leader_email = models.EmailField(blank= False)

    mate2_name = models.CharField(verbose_name = "Mate 2 name", max_length= 50, blank= True)
    mate2_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    mate2_email = models.EmailField(blank=True)

    mate3_name = models.CharField(verbose_name="Mate 3 name", max_length=50, blank=True)
    mate3_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    mate3_email = models.EmailField(blank=True)

    mate4_name = models.CharField(verbose_name="Mate 4 name", max_length=50, blank=True)
    mate4_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    mate4_email = models.EmailField(blank=True)


    problem1_selected = models.ForeignKey(problems, related_name='ps1', verbose_name='Selected problem statement 1', on_delete=models.CASCADE, blank= False)
    solution1 = models.CharField(verbose_name="Solution", help_text="How will you solve it",max_length=500, blank=False)

    problem2_selected = models.ForeignKey(problems, related_name='ps2',verbose_name= 'Selected problem statement 2',  on_delete=models.CASCADE, blank=True)
    solution2 = models.CharField(verbose_name="Solution", help_text="How will you solve it", max_length=500, blank=True)

    problem3_selected = models.ForeignKey(problems,  related_name='ps3',verbose_name= 'Selected problem statement 3', on_delete=models.CASCADE, blank=True)
    solution3 = models.CharField(verbose_name="Solution", help_text="How will you solve it", max_length=500, blank=True)
    def __str__(self):
        return self.name