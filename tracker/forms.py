from django.forms import ModelForm
from django import forms
from .models import *

class DayDescriptionForm(ModelForm):
    class Meta:
        model = DayDescription
        fields = ['subject','body']
        labels = {
            'body':'How was your Day'
        }

    def __init__(self,*args,**kwargs):
        super(DayDescriptionForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
