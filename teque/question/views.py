from django.shortcuts import render
from django.views import generic, View
from .models import QuestionModel
from .forms import UpLoadImgForm
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required


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
    fields = ('title', 'content', 'idea', 'deadline', 'category', 'level', 'image_1', 'image_2', 'image_3', 'image_4')

    success_url = reverse_lazy('list')

#画像のアップロード
def edit_question_idea(request):
    if request.method != 'POST':
        form = UpLoadImgForm()
    else:
        form = UpLoadImgForm(request.POST, request.FILES)
        if form.is_valid():
            image_1 = form.cleaned_data['画像1']
            question_idea = QuestionModel()
            question_idea.image_1 = image_1
            question_idea.save()
    context = {
        'form': form
    }
    return render(request, 'teque/question/templates/question/create.html', context)

'''
def view_article(request,pk):
    template_name = "question/detail.html"
    try:
        article = models.QuestionModel.objects.get(pk=pk)
    except models.QuestionModel.DoesNotExist:
        raise Http404
    if request.method == "POST":
        # データベースに投稿されたコメントを保存
        models.Comment.objects.create(text=request.POST["text"],article=article) # 追記
    context = {"article": article}
    return render(request, template_name, context)
'''


@login_required  # 追加
def post_list(request):
    return render(request, 'question/post_list.html',  {})