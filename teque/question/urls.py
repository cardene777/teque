from django.urls import path
from .views import QuestionList, QuestionDetail, QuestionUpdate, QuestionDelete, QuestionCreate

urlpatterns = [
    path('list/', QuestionList.as_view(), name='list'),
    path('detail/<int:pk>/', QuestionDetail.as_view(), name='detail'),
    path('update/<int:pk>/', QuestionUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', QuestionDelete.as_view(), name='delete'),
    path('create/', QuestionCreate.as_view(), name='create'),
]