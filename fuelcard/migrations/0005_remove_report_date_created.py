# Generated by Django 2.1 on 2018-11-14 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuelcard', '0004_report_meter_movement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='date_created',
        ),
    ]