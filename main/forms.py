from django import forms
from . import models


class StatementForm(forms.Form):
    name = forms.CharField(label='Полное имя пациента')
    phone = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
