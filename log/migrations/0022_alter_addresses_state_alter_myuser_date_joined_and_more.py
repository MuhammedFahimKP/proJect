# Generated by Django 4.2.6 on 2023-11-04 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0021_alter_addresses_state_alter_myuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='state',
            field=models.CharField(choices=[('Kerala', 'Kerala'), ('Karnataka', 'Karnataka'), ('Tamilnadu', 'TamilNadu')], max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 12, 13, 41, 601421)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 12, 13, 41, 601421)),
        ),
    ]
