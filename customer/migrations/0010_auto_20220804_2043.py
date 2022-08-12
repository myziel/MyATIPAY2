# Generated by Django 3.2.4 on 2022-08-04 15:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20220804_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, verbose_name='username')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='customer.clevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Levels',
        ),
    ]