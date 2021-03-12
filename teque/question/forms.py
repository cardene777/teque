from django import forms

class CategoryForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        required=True,
        widget=forms.widgets.Select
    )