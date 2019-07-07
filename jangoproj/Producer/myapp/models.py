from django.db import models

# Create your models here.

class Place(models.Model):
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.IntegerField()

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20)
    contactNo = models.IntegerField()
    rating = models.CharField(max_length = 20)
    owner = models.CharField(max_length = 20)
    place = models.OneToOneField(Place,
                                 on_delete=models.CASCADE,
                                 primary_key=True)

class Waiter(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    contactNo = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField()
    places = models.ManyToManyField(Place)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    waiter = models.ManyToManyField(Waiter)

# 'E:\\python_my_practice\\jangoproj\\Producer\\myapp\\'