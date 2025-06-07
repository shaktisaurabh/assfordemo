from django import forms
from django.core import validators

class ExampleForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100,validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(20)
    ])
    password = forms.CharField(widget=forms.PasswordInput)