# Generated by Django 5.1 on 2024-08-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='time_create',
            new_name='created_at',
        ),
    ]
