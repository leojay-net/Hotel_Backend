# Generated by Django 3.2.18 on 2023-08-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0003_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.CharField(default='462cbe584ea44888b9975d7e7e3df1cd', max_length=64, primary_key=True, serialize=False),
        ),
    ]
