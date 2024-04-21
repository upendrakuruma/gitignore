from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=55)
    age = models.IntegerField()
    cource = models.CharField(max_length=55)
    place = models.CharField(max_length=55)