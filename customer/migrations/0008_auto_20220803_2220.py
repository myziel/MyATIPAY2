# Generated by Django 3.2.4 on 2022-08-03 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20220803_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='lft',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='rght',
            field=models.IntegerField(blank=True),
        ),
    ]