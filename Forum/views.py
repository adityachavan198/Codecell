from django.shortcuts import render
from Forum.models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def forum_home(request, *args, **kwargs):
    question_list = Forum_question.objects.all().order_by('-asked_on')
    return render(request,'Forum/Forum_home.html',{'question_list':question_list})

class Ask_question(CreateView):
    template_name = "Forum/askquestion.html"
    model = Forum_question
    fields = ['question','description','topic']
    success_url = reverse_lazy('forum_home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        
        form.instance.user = self.request.user
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class Add_answer(CreateView):
    template_name = "Forum/add_answer.html"
    model = Forum_answer
    fields = ['answer',]
    success_url = reverse_lazy('forum_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question = Forum_question.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def answer_list(request, *args, **kwargs):
    question = Forum_question.objects.all().filter(pk = kwargs['pk'])[0]
    answers = Forum_answer.objects.all().filter(question = question).order_by('-answered_on')
    return render(request,'Forum/answer_list.html',{'answer':answers, 'question':question})