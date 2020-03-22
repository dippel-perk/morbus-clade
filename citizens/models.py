from django.db import models
from datetime import datetime, timedelta

from django.utils.crypto import get_random_string
from phonenumber_field.modelfields import PhoneNumberField


class Citizen(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField()
    telephone = PhoneNumberField()

    date_of_birth = models.DateField()

    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)

    def to_dict(self):
        return dict(
            address=self.address,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            telephone=str(self.telephone),
            date_of_birth=str(self.date_of_birth),
            zip_code=self.zip_code,
            city=self.city)


def one_week_hence():
    return datetime.now() + timedelta(days=7)


def generate_token():
    return get_random_string(64)


class AccessToken(models.Model):
    token = models.CharField(max_length=64, default=generate_token, primary_key=True)

    citizen = models.OneToOneField(Citizen, on_delete=models.CASCADE, related_name="access_token")
    is_write = models.BooleanField(default=False)

    expired = models.DateTimeField(default=one_week_hence)


class ContactPerson(models.Model):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

    INTENSITY_CHOICES = [
        (LOW, 'Gering'),
        (MEDIUM, 'Mittelstark'),
        (HIGH, 'Hoch'),
    ]

    citizen = models.ForeignKey(Citizen, related_name="contact_persons", on_delete=models.CASCADE)
    last_contact = models.DateTimeField(default=one_week_hence)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField()
    telephone = PhoneNumberField()

    intensity = models.IntegerField(choices=INTENSITY_CHOICES, default=LOW)

    description = models.TextField()

    @property
    def is_intensity_low(self):
        return self.intensity == ContactPerson.LOW

    @property
    def is_intensity_medium(self):
        return self.intensity == ContactPerson.MEDIUM

    @property
    def is_intensity_high(self):
        return self.intensity == ContactPerson.HIGH
