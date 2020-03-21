from django.db import models
from django.contrib.auth.models import AbstractUser
from citizens.models import Citizen


class User(AbstractUser):

    display_name = models.CharField(max_length=100, default="Anonym")

    is_health_department = models.BooleanField(default=False)
    is_laboratory = models.BooleanField(default=False)
    is_test_station = models.BooleanField(default=False)

    longitude = models.FloatField()
    latitude = models.FloatField()


class Test(models.Model):
    POSITIVE = 1
    NEGATIVE = 0
    PENDING = -1

    RESULT_CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
        (PENDING, 'Pending'),
    ]

    citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE, related_name="test")

    test_station = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commissioned_tests")
    laboratory = models.ForeignKey(User, on_delete=models.CASCADE, related_name="examined_tests")

    result = models.IntegerField(
        choices=RESULT_CHOICES,
        default=PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_positive(self):
        return self.result == Test.POSITIVE

    @property
    def is_negative(self):
        return self.result == Test.NEGATIVE

    @property
    def is_pending(self):
        return self.result == Test.PENDING