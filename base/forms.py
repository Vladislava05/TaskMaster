from django import forms

from django.forms import ModelForm

from .models import Task



        
class PositionForm(forms.Form):
    position = forms.CharField()

class DateInput(forms.DateTimeInput):
    input_type = 'date'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','complete', 'due_date']
        widgets = {
            'due_date': DateInput,
        }


