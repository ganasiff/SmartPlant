from django.db import models
from django.urls import reverse
# Create your models here.

class Settings(models.Model):
    
    HMI = 'HMI'
    CONTROLLER = "Controller"
    MASTER_CONTROLLER = "Master Controller"    
    ROLES = [
        (HMI , 'HMI'),
        (CONTROLLER , "Controller"),
        (MASTER_CONTROLLER , "Master Controller"),
    ]

    OK = 'OK'
    COMISSIONED ='COMISSIONED'
    UNCOMISSIONED = 'UNCOMISSIONED'
    FAULT = "FAULT"
    OFFLINE = "OFFLINE"

    STATUS_LIST = [
        (OK , 'OK'),
        (COMISSIONED , "COMISSIONED"),
        (UNCOMISSIONED , "UNCOMISSIONED"),
        (FAULT , "FAULT"),
        (OFFLINE , "OFFLINE"),
    ]


    
    role = models.CharField(
        max_length=len(MASTER_CONTROLLER),
        choices=ROLES,
        default=CONTROLLER
    )
    name = models.TextField()
    description = models.TextField()
    status = models.CharField(
        max_length=len(UNCOMISSIONED),
        choices=STATUS_LIST,
        default=UNCOMISSIONED
    )
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('settings')