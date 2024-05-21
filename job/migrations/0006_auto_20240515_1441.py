# Generated by Django 3.2.4 on 2024-05-15 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_alter_expenses_model_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_payment',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='network_payment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='other_source',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
    ]