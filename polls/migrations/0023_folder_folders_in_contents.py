# Generated by Django 4.0.4 on 2022-08-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_remove_choice_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='folders_in_contents',
            field=models.TextField(default=''),
        ),
    ]
