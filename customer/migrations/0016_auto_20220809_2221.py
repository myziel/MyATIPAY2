# Generated by Django 3.2.4 on 2022-08-09 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_auto_20220808_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogin',
            name='login_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 8, 9)),
        ),
        migrations.AlterField(
            model_name='customerlogin',
            name='login_time',
            field=models.TimeField(blank=True, default='22:21:17'),
        ),
    ]
