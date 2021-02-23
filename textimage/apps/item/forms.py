from django import forms
from .models import TextModel, ImageModel


class CreateItemForm(forms.ModelForm):

    class Meta:
        model = TextModel
        fields = ('title', )


class UpdateItemForm(forms.ModelForm):
    images = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))

    class Meta:
        model = TextModel
        fields = ('title', 'content',)
