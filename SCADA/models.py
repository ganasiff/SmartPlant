from django.db import models

# Create your models here.

class Settings(models.Model):
    role = models.TextField()
    name = models.TextField()
    description = models.TextField()