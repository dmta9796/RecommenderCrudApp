from django.db import models


class User(models.Model):
    firstname = models.charfield(max_length = 32)
    lastname = models.charfield(max_length = 32)
    city = models.charfield(max_length = 50)
    stateregion = models.charfield(max_length = 50)
    country = models.charfield(max_length = 50)

class product(models.Model):
    productname = models.charfield(max_length = 50)
