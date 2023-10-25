# Generated by Django 4.2.4 on 2023-10-15 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_alter_myuser_date_joined_alter_myuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 15, 22, 30, 0, 560156)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 15, 22, 30, 0, 560156)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]