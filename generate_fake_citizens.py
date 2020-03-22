from faker import Faker
import random as rd
from datetime import datetime, timedelta
from django.utils.crypto import get_random_string
import json

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = rd.randrange(int_delta)
    return start + timedelta(seconds=random_second)

fake = Faker('de_DE')

test_stations = [2, 3, 4, 5, 6]
labs = [7]

contact_person_current_id = 0

RESULT_CHOICES = [
    (1, 'Positive'),
    (0, 'Negative'),
    (-1, 'Pending'),
]

INTENSITY_CHOICES = [0, 1, 2]

def one_week_before():
    return datetime.now() - timedelta(days=7)

def three_weeks_hence():
    return datetime.now() + timedelta(days=21)


def generate_model(pk, model, data):
    return dict(pk=pk, model=model, fields=data)


def generate_access_token(pk):
    return generate_model(pk, "citizens.AccessToken", dict(token=get_random_string(64),
                                                           citizen=pk,
                                                           is_write=True,
                                                           expired=str(three_weeks_hence())))


def generate_test(pk):
    return generate_model(pk, "health.Test", dict(citizen=pk,
                                                  result=rd.choice(RESULT_CHOICES)[0],
                                                  test_station=rd.choice(test_stations),
                                                  laboratory=rd.choice(labs),
                                                  created_at=str(datetime.now()),
                                                  updated_at=str(datetime.now())))


"""citizen = models.ForeignKey(Citizen, related_name="contact_persons", on_delete=models.CASCADE)
    last_contact = models.DateTimeField(default=one_week_hence)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField()
    telephone = PhoneNumberField()

    intensity = models.IntegerField(choices=INTENSITY_CHOICES, default=LOW)

    description = models.TextField()"""


def generate_contact_person(pk):
    global contact_person_current_id
    contact_person_current_id += 1
    return generate_model(contact_person_current_id, "citizens.ContactPerson",
                          dict(first_name=fake.first_name(),
                               last_name=fake.last_name(),
                               citizen=pk,
                               email=fake.email(),
                               telephone="+49176" + str(rd.randint(10000000, 99999999)),
                               intensity=rd.choice(INTENSITY_CHOICES),
                               description=fake.text()[0:200],
                               last_contact=str(random_date(one_week_before(), datetime.now()))
                               ))


def generate_citizen(pk):
    return generate_model(pk, "citizens.Citizen", dict(first_name=fake.first_name(),
                                                       last_name=fake.last_name(),
                                                       email=fake.email(),
                                                       date_of_birth=str(fake.date_of_birth()),
                                                       address=fake.street_name() + " " + str(rd.randint(1, 100)),
                                                       zip_code=rd.choice([38100, 38101, 38102, 38103, 38104, 38105]),
                                                       telephone="+49176" + str(rd.randint(10000000, 99999999)),
                                                       city="Braunschweig"
                                                       ))


output = []
for i in range(100):
    output.append(generate_citizen(i))
    output.append(generate_access_token(i))
    output.append(generate_test(i))

    for j in range(rd.randint(3,15)):
        output.append(generate_contact_person(i))

with open("base_date.json", "w") as f:
    json.dump(output, f)
