# Generated by Django 3.2.18 on 2023-08-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0002_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.CharField(default='b6ece9f447c444a9b7df2951a5c0143d', max_length=64, primary_key=True, serialize=False),
        ),
    ]
