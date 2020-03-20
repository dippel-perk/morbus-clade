from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_health_department = models.BooleanField(default=False)
    is_laboratory = models.BooleanField(default=False)
    is_test_station = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()