# Generated by Django 2.2.6 on 2020-02-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_user_data_credit_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_data',
            name='phone_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
