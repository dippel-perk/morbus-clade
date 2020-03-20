from django.db import models


class Citizen(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField()

    date_of_birth = models.DateField()

    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)


