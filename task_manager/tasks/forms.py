from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'photos', 'priority', 'is_complete']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['due_date'].widget.attrs.update({'class': 'form-control datepicker'})
        self.fields['photos'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_complete'].widget.attrs.update({'class': 'form-check-input'})
