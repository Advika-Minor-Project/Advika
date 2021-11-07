from django.db import models
import uuid
from users.models import Profile
# Create your models here.
class DayDescription(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL,related_name='tracks')
    date = models.DateField(auto_now=True)
    subject = models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner','date']]
        ordering = ['date']

    def __str__(self):
        return self.subject