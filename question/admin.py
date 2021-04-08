from django.contrib import admin
from question.models import QuestionModel, Comment

# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(Comment)