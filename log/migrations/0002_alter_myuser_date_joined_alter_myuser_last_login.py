# Generated by Django 4.2.4 on 2023-10-08 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 22, 51, 53, 4905)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 22, 51, 53, 4905)),
        ),
    ]