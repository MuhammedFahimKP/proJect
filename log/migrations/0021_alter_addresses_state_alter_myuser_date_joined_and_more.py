# Generated by Django 4.2.6 on 2023-11-04 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0020_alter_addresses_place_alter_myuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='state',
            field=models.CharField(choices=[('KERALA', 'Kerala'), ('KARNATAKA', 'Karnataka'), ('TAMILNADU', 'TamilNadu')], max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 9, 41, 2, 239632)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 9, 41, 2, 239632)),
        ),
    ]
