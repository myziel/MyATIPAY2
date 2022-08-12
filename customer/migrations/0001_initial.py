# Generated by Django 3.2.4 on 2022-08-01 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('upliner', models.IntegerField()),
                ('ref_id', models.IntegerField()),
                ('position', models.CharField(choices=[('Right', 'Right'), ('Left', 'Left')], default='Right', max_length=5)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerLogin',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('login_time', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
            options={
                'verbose_name_plural': 'Customer Login',
            },
        ),
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('last_login', models.CharField(blank=True, max_length=100)),
                ('is_active', models.CharField(blank=True, max_length=100)),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='static/user_photos/')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('alternate_mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField(blank=True)),
                ('zipcode', models.CharField(blank=True, max_length=6, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('cnic', models.CharField(blank=True, max_length=50, null=True)),
                ('cp_points', models.FloatField(blank=True, default=0.0, null=True)),
                ('t_personal_earning', models.FloatField(blank=True, default=0.0, null=True)),
                ('withdrawel_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('ewallet', models.FloatField(blank=True, default=0.0, null=True)),
                ('city', models.ForeignKey(default=86, on_delete=django.db.models.deletion.CASCADE, to='main.cities')),
                ('country', models.ForeignKey(default=167, on_delete=django.db.models.deletion.CASCADE, to='main.countries')),
                ('state', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.states')),
            ],
            options={
                'verbose_name_plural': 'Customer Detail',
            },
        ),
    ]