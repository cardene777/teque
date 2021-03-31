from django.db import models
from django.utils import timezone

# Create your models here.

class QuestionModel(models.Model):
    class Meta:
        verbose_name = "Todoリスト"
        verbose_name_plural = 'Todoリスト'

    CATEGORY_CHOICES = (
    (1, 'エラー対処'),
    (2, '技術質問'),
    )

    LEVEL_CHOICES = (
    (1, 'より深く'),
    (2, '対処法のみ'),
    )

    title = models.CharField(
        verbose_name="質問タイトル",
        max_length=50,
    )
    content = models.TextField(
        verbose_name="質問内容"
    )

    idea = models.TextField(
        verbose_name="自分の認識or行った対処法"
    )

    deadline = models.DateTimeField(
        verbose_name="期日",
        default=timezone.now
    )

    #質問カテゴリ
    category = models.IntegerField(
        verbose_name = "質問カテゴリ",
        choices=CATEGORY_CHOICES
    )

    #して欲しい回答のやり方
    level = models.IntegerField(
        verbose_name = "回答レベル",
        choices=LEVEL_CHOICES,
        blank=True
    ) 

    #画像のアップロード
    image_1 = models.ImageField(
        verbose_name = '画像1',
        upload_to = 'images/',
        blank=True,
        default='images/IMG_1045.JPG'
    )

    image_2 = models.ImageField(
        verbose_name = '画像2',
        upload_to = 'images/',
        blank=True
    )

    image_3 = models.ImageField(
        verbose_name = '画像3',
        upload_to = 'images/',
        blank=True
    )

    image_4 = models.ImageField(
        verbose_name = '画像4',
        upload_to = 'images/',
        blank=True
    )

    def __str__(self):
        return self.title  

#コメント機能
class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(to=QuestionModel, related_name='comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.text


