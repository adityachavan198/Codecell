from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.core.validators import RegexValidator

# Create your models here.

categories = (
    ('Machine Learning / Artificial Intelligence','Machine Learning / Artificial Intelligence'),
    ('Blockchain','Blockchain'),
    ('Web Development','Web Development'),
    ('Android Application', 'Android Application'),
)

year = (
    ('First Year', 'First Year'),
    ('Second Year', 'Second Year'),
    ('Third Year', 'Third Year'),
    ('Fourth Year', 'Fourth Year'),
)

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")

class problems(models.Model):

    title = models.CharField(verbose_name= "Title", max_length = 50, blank = False)

    statement = models.CharField(verbose_name = "Problem Statement", max_length = 500, blank = False)

    Category = models.CharField(verbose_name="Category", max_length=50, default='Machine Learning',
                             choices=categories)

    def __str__(self):
        return self.title

class team(models.Model):

    name = models.CharField(verbose_name = "Team Name", max_length= 50, blank= False)

    college_name = models.CharField(verbose_name = "College Name", default="RGIT",  max_length= 100, blank= False)

    size = models.PositiveSmallIntegerField(blank = False, default = 4, verbose_name = "Team Size", help_text = "No. of player in a team", validators = [MaxValueValidator(4),MinValueValidator(2)] )

    leader_name = models.CharField(verbose_name = "Team Leader name",  max_length= 50, blank= False)

    leader_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)

    leader_email = models.EmailField(blank= False)

    leader_year = models.CharField(verbose_name = "Leader Current Year", default = "TE", max_length= 20, blank= False, choices=year)

    mate2_name = models.CharField(verbose_name = "Mate 2 name", max_length= 50, blank= False)
    mate2_number = models.CharField(validators=[phone_regex], max_length=15, blank=False)
    mate2_email = models.EmailField(blank=False)
    mate2_year = models.CharField(verbose_name="Mate 2 Current Year", default = "TE", max_length=20, blank=False, choices=year)

    mate3_name = models.CharField(verbose_name="Mate 3 name", max_length=50, blank=True)
    mate3_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    mate3_email = models.EmailField(blank=True)
    mate3_year = models.CharField(verbose_name="Mate 3 Current Year", max_length=20, blank=True, choices=year)

    mate4_name = models.CharField(verbose_name="Mate 4 name", max_length=50, blank=True)
    mate4_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    mate4_email = models.EmailField(blank=True)
    mate4_year = models.CharField(verbose_name="Mate 4 Current Year", max_length=20, blank=True, choices=year)

    domain1 = models.CharField(verbose_name="Domain Preference 1", max_length=50, blank=False, choices=categories)
    domain2 = models.CharField(verbose_name="Domain Preference 2", max_length=50, blank=False, choices=categories)
    domain3 = models.CharField(verbose_name="Domain Preference 3", max_length=50, blank=False, choices=categories)

    def __str__(self):
        return self.name