# Generated by Django 3.2.4 on 2022-08-04 16:24

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_binary'),
    ]

    operations = [
        migrations.CreateModel(
            name='CBinary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, verbose_name='username')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='customer.cbinary')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Binary',
        ),
    ]
