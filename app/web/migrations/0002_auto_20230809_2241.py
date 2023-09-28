# Generated by Django 3.2.18 on 2023-08-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logroom',
            options={'ordering': ['booked_date']},
        ),
        migrations.RenameField(
            model_name='logroom',
            old_name='date_booked',
            new_name='booked_date',
        ),
        migrations.RenameField(
            model_name='logroom',
            old_name='date_end',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='logroom',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]