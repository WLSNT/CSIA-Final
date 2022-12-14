# Generated by Django 4.0.4 on 2022-09-10 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0048_alter_folder_creator_alter_folder_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.AlterField(
            model_name='folder',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 10, 21, 11, 23, 246732)),
        ),
        migrations.RemoveField(
            model_name='folder',
            name='tags',
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default='None', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='folder',
            name='tags',
            field=models.ManyToManyField(to='polls.tag'),
        ),
    ]
