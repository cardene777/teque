from django.shortcuts import render
from django.views import generic
from .models import QuestionModel
from django.urls import reverse_lazy

# Create your views here.

class QuestionList(generic.ListView):
    template_name = 'question/list.html'
    model = QuestionModel

class QuestionDetail(generic.DetailView):
    template_name = 'question/detail.html'
    model = QuestionModel

class QuestionUpdate(generic.UpdateView):
    template_name = 'question/update.html'
    model = QuestionModel
    fields = ('title', 'content', 'deadline')
    success_url = reverse_lazy('list')

class QuestionDelete(generic.DeleteView):
    template_name = 'question/delete.html'
    model = QuestionModel

    success_url = reverse_lazy('list')

class QuestionCreate(generic.CreateView):
    template_name = 'Question/create.html'
    model = QuestionModel
    fields = ('title', 'content', 'deadline')

    success_url = reverse_lazy('list')