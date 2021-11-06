from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from .models import *

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title','featured_image','description','source_link','tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),

        }

    def __init__(self,*args,**kwargs):
        super(BlogForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
