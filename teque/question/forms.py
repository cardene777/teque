from django import forms
from PIL import Image
class UpLoadImgForm(forms.Form):
    image_1 = forms.QuestionModel(required=True)
    image_2 = forms.QuestionModel(required=True)
    image_3 = forms.QuestionModel(required=True)
    image_4 = forms.QuestionModel(required=True)

class CategoryForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        required=True,
        widget=forms.widgets.Select
    )