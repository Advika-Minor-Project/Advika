from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name*',
            'email':'Email address*',

        }

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['required'] = 'required'
            
class RoleForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
        labels={
            'role':'Role*'
        }

    def __init__(self, *args, **kwargs):
        super(RoleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['required'] = 'required'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_linkedin', 'social_twitter',
                  'social_youtube', 'social_website']
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'
        labels = {
            'qualification':'Qualification*',
            'description':'Description*'
        }
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(QualificationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['required'] = 'required'

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        labels= {
            'name':'Name*',
            'email':'Email address*',
            'subject':'Subject*',
            'body':'Description*'
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['required'] = 'required'

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name','email','date','time','subject','body']
        labels = {
            'name':'Name*',
            'email':'Email address*',
            'date':'Date*',
            'time':'Time*',
            'subject':'Subject*',
            'body':'Description*'
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs['required'] = 'required'