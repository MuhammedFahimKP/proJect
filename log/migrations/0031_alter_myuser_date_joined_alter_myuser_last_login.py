# Generated by Django 4.2.6 on 2023-11-07 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0030_alter_myuser_date_joined_alter_myuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 7, 20, 6, 8, 614499)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 7, 20, 6, 8, 614499)),
        ),
    ]