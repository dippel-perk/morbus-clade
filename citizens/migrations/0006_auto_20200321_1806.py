# Generated by Django 3.0.2 on 2020-03-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizens', '0005_contactperson_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactperson',
            name='intensity',
            field=models.IntegerField(choices=[(0, 'Gering'), (1, 'Mittelstark'), (2, 'Hoch')], default=0),
        ),
    ]
