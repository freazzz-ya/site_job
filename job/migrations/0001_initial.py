# Generated by Django 3.2 on 2024-01-13 09:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_balance', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='balance money')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='last_updated')),
            ],
            options={
                'verbose_name': 'balance',
                'verbose_name_plural': 'balances',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='name djob')),
                ('busyness', models.CharField(choices=[('Main', 'Main job'), ('Part-time', 'Part-time job')], default='Part-time', max_length=256, verbose_name='busyness')),
                ('payment', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1, message='Не может быть меньше 1'), django.core.validators.MaxValueValidator(limit_value=100, message='Не может быть больше 100')], verbose_name='payment')),
                ('duration', models.CharField(choices=[('Day', 'working time duration - day'), ('Month', 'working time duration - month')], default='Day', max_length=256, verbose_name='duration')),
            ],
            options={
                'verbose_name': 'worker',
                'verbose_name_plural': 'workers',
                'ordering': ('name',),
            },
        ),
    ]
