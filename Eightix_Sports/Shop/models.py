from django.db import models

# Create your models here.


class Kids(models.Model):

    name = models.CharField(max_length=50)
    dec = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Clothes(models.Model):

    name = models.CharField(max_length=50)
    dec = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Cardio(models.Model):

    name = models.CharField(max_length=50)
    dec = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Gym_equipments(models.Model):

    name = models.CharField(max_length=50)
    dec = models.CharField(max_length=500)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return self.name
