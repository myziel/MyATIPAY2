# Generated by Django 3.2.4 on 2022-08-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20220802_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='parent',
            new_name='ref_id',
        ),
    ]