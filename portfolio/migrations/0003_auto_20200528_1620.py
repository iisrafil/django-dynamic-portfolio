# Generated by Django 3.0.6 on 2020-05-28 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='degere',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='resume',
            old_name='Description',
            new_name='description',
        ),
    ]
