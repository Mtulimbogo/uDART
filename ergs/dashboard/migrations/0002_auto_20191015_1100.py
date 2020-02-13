# Generated by Django 2.2.6 on 2019-10-15 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='sensor_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rfid1_readings', models.CharField(max_length=220)),
                ('rfid2_readings', models.CharField(max_length=220)),
                ('hall_effect_readings', models.FloatField()),
                ('current_values1', models.FloatField()),
                ('current_values2', models.FloatField()),
                ('battery_health1', models.FloatField()),
                ('battery_health2', models.FloatField()),
                ('train_id', models.FloatField()),
                ('gate_id', models.FloatField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='train_detail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('train_name', models.CharField(max_length=50)),
                ('tag_id', models.FloatField()),
                ('train_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gate_name', models.CharField(max_length=50)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.location')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.question')),
            ],
        ),
        migrations.CreateModel(
            name='admin_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
                ('nida_no', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=22)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]