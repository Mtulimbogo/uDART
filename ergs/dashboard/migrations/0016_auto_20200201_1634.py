# Generated by Django 2.2.6 on 2020-02-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20200201_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus_station',
            name='station_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='entry_logs',
            name='uuid_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exit_logs',
            name='uuid_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recharge_logs',
            name='uuid_number',
            field=models.IntegerField(),
        ),
    ]
