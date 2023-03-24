from django.db import models

# Create your models here.
class Gym(models.Model):
    uname = models.CharField(max_length = 25)
    phone = models.IntegerField()
    email = models.TextField()
    fdate = models.DateField()
    tdate = models.DateField()
    gender = models.TextField()