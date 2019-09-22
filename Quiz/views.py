from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404,render
from Quiz.models import *

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