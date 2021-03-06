# Generated by Django 2.2.6 on 2020-02-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20200201_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('type_of_registration', models.CharField(max_length=50)),
                ('registration_number', models.CharField(max_length=50)),
                ('password', models.CharField(default=0, max_length=10)),
            ],
        ),
    ]
