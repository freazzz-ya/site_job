# Generated by Django 5.0.1 on 2024-01-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_neural_network_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neural_network',
            name='description',
            field=models.TextField(default='Дефолтное описание', max_length=10000, verbose_name='Описание'),
        ),
    ]
