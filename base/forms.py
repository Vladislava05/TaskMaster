from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.forms import ModelForm, Textarea

from .models import Task, Notion

class PositionForm(forms.Form):
    position = forms.CharField()

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'complete']
        widgets = {
            'due_date': DateInput,
        }

class NotionForm(ModelForm):
    class Meta:
        model = Notion
        fields = ['title', 'body']
       


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name=forms.CharField(max_length=40)
    last_name=forms.CharField(max_length=40)
    
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name', 'email']

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name=forms.CharField(max_length=40)
    last_name=forms.CharField(max_length=40)
    
    class Meta:
        model = User
        fields=['username', 'first_name', 'last_name',  'email']
        