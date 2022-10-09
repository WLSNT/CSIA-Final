# Generated by Django 4.0.4 on 2022-08-12 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_remove_profile_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='Folder',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='folder',
        ),
        migrations.AddField(
            model_name='choice',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.tags'),
        ),
    ]