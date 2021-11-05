from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    choices = (
        ('Mental Health Specialist','Mental Health Specialist'),
        ('User','User')
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=50,choices=choices,default='Select your role',null=True,blank=True)
    verified = models.BooleanField(default=False,null=True,blank=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to = "profiles/",default = 'profiles/user-default.png')
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Qualification(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.qualification)

class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    recipient = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name = 'messages')
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    is_read = models.BooleanField(default=False,null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read','-created']

class Appointment(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    recipient = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name = 'appointments')
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.subject
    

