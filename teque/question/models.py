from django.db import models
from django.utils import timezone

# Create your models here.

class QuestionModel(models.Model):
    class Meta:
        verbose_name = "Todoリスト"
        verbose_name_plural = 'Todoリスト'

    title = models.CharField(
        verbose_name="タイトル",
        max_length=50,
    )
    content = models.TextField(
        verbose_name="内容"
    )
    deadline = models.DateTimeField(
        verbose_name="期日",
        default=timezone.now
    )

    def __str__(self):
        return self.title