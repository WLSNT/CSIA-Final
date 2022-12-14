# Generated by Django 4.0.4 on 2022-09-08 16:15

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0034_alter_folder_pub_date_alter_folder_pub_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='folders_in_contents',
        ),
        migrations.AlterField(
            model_name='folder',
            name='pub_date',
            field=models.DateField(default=datetime.date(2022, 9, 9)),
        ),
        migrations.AlterField(
            model_name='folder',
            name='pub_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
