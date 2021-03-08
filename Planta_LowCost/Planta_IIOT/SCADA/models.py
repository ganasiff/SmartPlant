from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TransmisorESP(models.Model):
    id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField('date published')
    label = models.CharField(max_length=200, default="")
    datapoint = models.CharField(
        max_length=20,
        default="0",
    )
    def __str__(self):
        return 'id: '+str(self.id)+'/label: '+self.label+'/data: '+self.datapoint

class Datapoint(models.Model):
    id = models.IntegerField(primary_key=True)
    channel = models.IntegerField(default=0)
    timestamp = models.DateTimeField('date published')
    transmisor = models.CharField(max_length=200, default="")
    label = models.CharField(max_length=200, default="")
    tag = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")
    data = models.CharField(
        max_length=20,
        default="0",
    )
    def __str__(self):
        return 'id: '+str(self.id)+'/label: '+self.label+'/data: '+self.datapoint

   
