# Generated by Django 4.2.4 on 2023-10-15 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_alter_myuser_date_joined_alter_myuser_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 15, 22, 54, 0, 76728)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 15, 22, 54, 0, 76728)),
        ),
    ]