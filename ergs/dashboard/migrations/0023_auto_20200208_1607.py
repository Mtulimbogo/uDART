# Generated by Django 2.2.6 on 2020-02-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20200208_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge',
            name='place_of_recharge',
            field=models.CharField(default=0, max_length=220),
        ),
    ]