# Generated by Django 2.2.6 on 2019-10-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20191015_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]