# Generated by Django 4.1 on 2022-09-09 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0039_alter_choice_author_alter_choice_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]