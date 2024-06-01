# Generated by Django 3.2.4 on 2024-05-15 22:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_expenses_model_variety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_payment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='network_payment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='other_source',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
    ]
