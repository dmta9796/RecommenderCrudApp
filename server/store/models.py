from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length = 32)
    lastname = models.CharField(max_length = 32)
    city = models.CharField(max_length = 50)
    stateregion = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)

class Product(models.Model):
    productname = models.CharField(max_length = 32)
    productdetails = models.CharField(max_length = 1000)
    productweight = models.IntegerField()
    productorigin = models.CharField(max_length = 30)
