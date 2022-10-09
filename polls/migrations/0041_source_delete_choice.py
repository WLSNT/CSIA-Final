# Generated by Django 4.1 on 2022-09-09 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0040_alter_choice_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('pub_date', models.DateField(null=True)),
                ('source_url', models.URLField(null=True)),
                ('description', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('folders_contained_in', models.ManyToManyField(to='polls.folder')),
                ('tags', models.ManyToManyField(null=True, to='polls.tags')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]