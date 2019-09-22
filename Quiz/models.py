import re   # regex for urls
from django.db import models
from model_utils.managers import InheritanceManager
from django.core.validators import MaxValueValidator

# Create your models here.

class CategoryManager(models.Manager):

    def new_category(self,category):
        new_category = self.create(category=re.sub('\s+','-',category).lower())
        new_category.save()
        return new_category

class Category(models.Model):

    category = models.CharField( verbose_name="Category", max_length = 250, blank = True, unique = True, null = True)

    # If we need to add Images in our Project we will need to install pillow.
    image = models.ImageField(upload_to = 'Images/Categories/', blank = True, null = True, verbose_name = "Image")

    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class SubCategory(models.Model):

    sub_category = models.CharField(verbose_name="Sub_Category", max_length = 250, blank = True, null = True)

    category = models.ForeignKey(Category, null = True, blank = True, verbose_name = "Category", on_delete=models.CASCADE)

    objects = CategoryManager()

    class Meta:
        verbose_name = "Sub-Category"
        verbose_name_plural = "Sub-Categories"

    def __str__(self):
        return self.sub_category + " ( " + self.category.category + " ) "


class Quiz(models.Model):
    ''' Quiz is onetomany modeled to Questions '''

    title = models.CharField(verbose_name= "Title", max_length = 50, blank = False)

    description = models.TextField(verbose_name = "Description", blank = True, help_text = "Quiz description")

    url = models.SlugField(max_length = 60, blank = False, help_text = "A user friendly url", verbose_name = "User Friendly Url")

    category = models.ForeignKey(Category, null = True, blank = True, verbose_name = "Category", on_delete = models.CASCADE)

    random_order = models.BooleanField(blank = False, default = True, verbose_name = "Random Order", help_text = "Display the questions in Random Order ?")

    max_questions = models.PositiveIntegerField(blank = True, null = True, verbose_name = "Max_questions", help_text = "Number of questions to be displayed on each attempt")

    single_attempt = models.BooleanField(blank = False, default = False, help_text = "If selected, user will be allowed only one attempt for this quiz", verbose_name = "Single Attempt")

    pass_mark = models.PositiveSmallIntegerField(blank = True, default = 0, verbose_name = "Passing Marks", help_text = "Percentage required to pass", validators = [MaxValueValidator(100)])

    success_text = models.TextField(blank = True, help_text = "Displayed if user passes.", verbose_name = "Success Text")

    fail_text = models.TextField(blank = True, help_text = "Displayed if user fails", verbose_name = "Fail Text")

    draft = models.BooleanField(blank = True, default = False, verbose_name = "Draft", help_text = "Quiz won't be available to student if this is selected, only for internal assessment this quiz will be available")

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        ''' overriding the default save because we need to slash the whitespaces in urls '''

        self.url = re.sub('\s+', '-', self.url).lower()
        self.url = ''.join(letter for letter in self.url if letter.isalnum() or letter == '-')

        super(Quiz, self).save(force_insert, force_update, *args, **kwargs)

    def get_questions(self):
        return self.question_set.all().select_subclasses()

    

class Question(models.Model):
    ''' Base class for all question types. Question properties are here '''

    quiz = models.ManyToManyField(Quiz, verbose_name = "Quiz", blank = True)

    category = models.ForeignKey(Category, verbose_name = "Category", blank = True, null = True, on_delete = models.CASCADE)

    sub_category = models.ForeignKey(SubCategory, verbose_name = "Sub-Category", blank = True, null = True, on_delete = models.CASCADE)

    # same as before, needs pillow
    figure = models.ImageField(upload_to='Images/Questions/', blank = True, null = True, verbose_name = "Question Image")

    content = models.CharField(max_length = 1000, blank = False, help_text = "Enter the Question (text)", verbose_name = 'Question')

    explanation = models.TextField(max_length = 2000, blank = True, help_text = "Explanation to be shown after the question is answered ", verbose_name = "Explanation")

    objects = InheritanceManager()

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['category']

        def __str__(self):
            return self.content
