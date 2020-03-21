# Generated by Django 3.0.2 on 2020-03-21 15:06

import citizens.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0003_citizen_telephone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_contact', models.DateTimeField(default=citizens.models.one_week_hence)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('description', models.TextField()),
                ('citizen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_persons', to='citizens.Citizen')),
            ],
        ),
    ]