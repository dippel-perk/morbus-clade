from django.db import models
from datetime import datetime, timedelta

from django.utils.crypto import get_random_string

class Citizen(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField()

    date_of_birth = models.DateField()

    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)

def one_week_hence():
    return datetime.now() + timedelta(days=7)

def generate_token():
    return get_random_string(64)

class AccessToken(models.Model):
    token = models.CharField(max_length=64, default=generate_token, primary_key=True)

    citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE)
    is_write = models.BooleanField(default=False)

    expired = models.DateTimeField(default=one_week_hence)


