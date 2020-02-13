# Generated by Django 2.2.6 on 2020-02-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20200205_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='control_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid_number', models.IntegerField()),
                ('recharged_amount', models.FloatField(default=0, max_length=220)),
                ('place_of_recharge', models.FloatField(default=0, max_length=220)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_data',
            name='vendor_name',
        ),
        migrations.RemoveField(
            model_name='vendor_data',
            name='password',
        ),
        migrations.AddField(
            model_name='user_data',
            name='vendor_id',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='vendor_data',
            name='vendor_id',
            field=models.CharField(default='', max_length=6, unique=True),
        ),
        migrations.AddField(
            model_name='vendor_data',
            name='vendor_password',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='national_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='uuid_number',
            field=models.IntegerField(),
        ),
    ]
