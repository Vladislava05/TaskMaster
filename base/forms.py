from django import forms
from django.forms import ModelForm, Textarea


class PositionForm(forms.Form):
    position = forms.CharField()
