# Generated by Django 2.2.6 on 2020-02-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_user_data_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_station',
            name='machine_id',
            field=models.IntegerField(),
        ),
    ]