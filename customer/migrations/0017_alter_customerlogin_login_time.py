# Generated by Django 3.2.4 on 2022-08-09 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_auto_20220809_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogin',
            name='login_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2022, 8, 9, 22, 23, 37, 977546)),
        ),
    ]
