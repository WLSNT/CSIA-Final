# Generated by Django 4.0.2 on 2022-04-07 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 4, 7, 12, 2, 28, 472002, tzinfo=utc), null=True),
        ),
    ]
