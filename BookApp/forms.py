from django import forms


class AddNewBookForm(forms.Form):
    name_book = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Name Book"}))
    name_author = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Name Author"}))
    detail = forms.CharField(
        max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', "placeholder": "detail"}))
