# Generated by Django 5.1 on 2024-08-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_alter_measurement_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
