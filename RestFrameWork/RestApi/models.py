from pickle import FALSE

from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()

    def __str__(self):
      return (self.email)

