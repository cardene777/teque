from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required  # 追加
def post_list(request):
    return render(request, 'testapp/post_list.html',  {})
