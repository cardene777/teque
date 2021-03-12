from django.shortcuts import render
from django.views import generic, View
from .models import QuestionModel
from django.urls import reverse_lazy
from . import forms

# Create your views here.

class QuestionList(generic.ListView):
    template_name = 'question/list.html'
    model = QuestionModel


class QuestionDetail(generic.DetailView):
    template_name = 'Question/detail.html'
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
    template_name = 'question/create.html'
    model = QuestionModel
    fields = ('title', 'content', 'idea', 'deadline')

    success_url = reverse_lazy('list')

class CategoryView(View):
    def get(self, request):
        form = forms.CategoryForm()
        form.fields['choice1'].choices = [
            ('1', 'エラー対処'),
            ('2', '技術質問 '),
        ]
        context = {
            'form': form
        }

        return render(request, 'create.html', context)

sample_choice_add_view = CategoryView.as_view()