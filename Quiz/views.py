from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404,render
from django.core.exceptions import PermissionDenied

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