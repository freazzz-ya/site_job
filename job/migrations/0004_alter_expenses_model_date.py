# Generated by Django 3.2.4 on 2024-05-15 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20240515_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses_model',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Дата'),
        ),
    ]
