# Generated by Django 4.2.7 on 2023-11-08 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0032_alter_myuser_date_joined_alter_myuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 9, 30, 41, 185910)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 9, 30, 41, 185910)),
        ),
    ]
