# Generated by Django 3.2.18 on 2023-08-08 07:29

import adminpage.utils
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogRoom',
            fields=[
                ('id', models.CharField(default=adminpage.utils.generate_id, max_length=64, primary_key=True, serialize=False)),
                ('user', models.CharField(blank=True, max_length=1000, null=True)),
                ('room_number', models.IntegerField()),
                ('date_booked', models.DateField(default=web.models.today)),
                ('date_end', models.DateField(default=web.models.today)),
                ('booked', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='date_created')),
            ],
            options={
                'ordering': ['date_booked'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(default=adminpage.utils.generate_id, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('price', models.IntegerField()),
                ('user', models.CharField(blank=True, max_length=1000, null=True)),
                ('room_number', models.IntegerField(unique=True)),
                ('url', models.URLField()),
                ('occupied', models.BooleanField(default=False)),
                ('booked_date', models.DateField(default=web.models.today)),
                ('available_date', models.DateField(default=web.models.today)),
                ('end_date', models.DateField(default=web.models.today)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='date_created')),
            ],
            options={
                'ordering': ['-room_number'],
            },
        ),
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='date_created')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='web.room')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
