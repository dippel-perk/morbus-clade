# Generated by Django 3.0.4 on 2020-03-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_auto_20200321_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(default='Anonym', max_length=100),
        ),
    ]
