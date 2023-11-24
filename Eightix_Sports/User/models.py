from django.db import models

# Create your models here.


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    phn_no = models.IntegerField()

    def __str__(self):
        return (self.username)


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    image = models.ImageField()
    quantity = models.IntegerField()
    section = models.CharField(max_length=45)

    def __str__(self):
        return (self.title)
