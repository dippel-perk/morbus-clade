# Generated by Django 3.0.2 on 2020-03-20 23:59

import citizens.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('token', models.CharField(default=citizens.models.generate_token, max_length=64, primary_key=True, serialize=False)),
                ('is_write', models.BooleanField(default=False)),
                ('expired', models.DateTimeField(default=citizens.models.one_week_hence)),
                ('citizen', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='citizens.Citizen')),
            ],
        ),
    ]
