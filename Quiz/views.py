from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import PermissionDenied
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from Quiz.models import *
from Quiz.forms import *

# Create your views here.

class Categories_list_view(ListView):
    model = Category

class View_Quizlist_by_Category(ListView):
    model = Quiz
    template_name = 'Quiz/Quiz_category_list_matching.html'
    context_object_name = 'quiz_list'

    def dispatch(self, request , *args, **kwargs):
        ''' dispatches a url request '''
        self.category = get_object_or_404(Category, category = self.kwargs['category_name'])

        return super(View_Quizlist_by_Category, self).dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        
        context = super(View_Quizlist_by_Category, self).get_context_data(**kwargs)

        context['category'] = self.category
        
        return context

    def get_queryset(self):
        queryset = super(View_Quizlist_by_Category, self).get_queryset()
        return queryset.filter(category = self.category, draft = False)
    
class Quiz_Detail_View(DetailView):
    model = Quiz
    slug_field = 'url'
    template_name = 'Quiz/quiz_detail.html'

    def get(self, request, *args, **kwargs):
        
        self.object = self.get_object()

        if self.object.draft and not request.user.has_perm('quiz.change_quiz'):
            return PermissionDenied
        
        context = self.get_context_data(object = self.object)
        return render(request,self.template_name,{'quiz':self.object})

class QuizAttempt(View):
    template_name = 'Quiz/attempt.html'
    Quiz_form = QuizForm

    def get(self, request, *args, **kwargs):
        ''' Process a get request  to attempt quiz '''
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        
        Quiz_form = self.Quiz_form(kwargs['quiz_name'])

        return render(request,self.template_name,{'Quiz_form':Quiz_form})

    
    def post(self, request, *args, **kwargs):
        ''' Process a post request after user has answered '''
        Quiz_form = self.Quiz_form(kwargs['quiz_name'],request.POST)

        if Quiz_form.is_valid():

            Current_quiz = Quiz.objects.all().filter(title = kwargs['quiz_name'])[0]
            Question_list = MCQ.objects.all().filter(quiz = Current_quiz)
            marks = 0
            for i in request.POST.keys():

                if i!='csrfmiddlewaretoken':
                    question_name =  Question_list.filter(content = i)[0]
                    answer = Answer.objects.all().filter(question = question_name).filter(content = request.POST[i])[0]
                    if answer.correct:
                        marks += question_name.marks 
                    
            print("The ",request.user,"Has scored ",marks, "in this quiz")       
            
            return HttpResponseRedirect(reverse('home'))
        