# Generated by Django 4.1 on 2022-09-09 01:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0041_source_delete_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='pub_time',
        ),
        migrations.AlterField(
            model_name='folder',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 9, 1, 39, 35, 582105)),
        ),
    ]