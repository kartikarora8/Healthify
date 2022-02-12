from django.forms import ModelForm, widgets
from django import forms
from .models import report

class ReportForm(ModelForm):
    class Meta:
        model = report
        fields = ['adhar','title', 'report']

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
 
        self.fields['adhar'].widget.attrs.update({'class' : 'input'})
        self.fields['title'].widget.attrs.update({'class' : 'input'})