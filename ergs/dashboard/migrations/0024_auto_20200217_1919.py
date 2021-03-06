# Generated by Django 2.2.6 on 2020-02-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20200208_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='credit_amount',
        ),
        migrations.AddField(
            model_name='bus_station',
            name='centre_latitude',
            field=models.FloatField(default=0, max_length=220),
        ),
        migrations.AddField(
            model_name='bus_station',
            name='centre_longitude',
            field=models.FloatField(default=0, max_length=220),
        ),
    ]
