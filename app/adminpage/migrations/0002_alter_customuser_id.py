# Generated by Django 3.2.18 on 2023-08-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.CharField(default='95bc6ffab91a4610a86f30e353048277', max_length=64, primary_key=True, serialize=False),
        ),
    ]
