# Generated by Django 3.1.4 on 2020-12-14 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='entry_points',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='reg_date',
        ),
    ]
