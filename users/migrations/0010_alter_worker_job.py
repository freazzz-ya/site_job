# Generated by Django 5.0.1 on 2024-01-19 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20240118_1847'),
        ('users', '0009_alter_worker_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='job',
            field=models.ManyToManyField(blank=True, default='безработный', null=True, related_name='job', to='job.job'),
        ),
    ]
