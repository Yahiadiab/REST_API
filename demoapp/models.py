from django.db import models

# Create your models here.

class Logger(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    age = models.IntegerField()