# Generated by Django 4.0.4 on 2022-09-10 03:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0045_remove_folder_creator_folder_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 11, 22, 34, 425632)),
        ),
    ]
