from django import forms
from .models import BookModel


class AddNewBookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ["name_book", "name_author", "detail"]
        widgets = {
            "name_book": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "name book..."}
            ),
            "name_author": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "name author..."}
            ),
            "detail": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "detail..."}
            ),
        }
