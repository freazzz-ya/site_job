# Generated by Django 5.0.1 on 2024-01-31 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_neural_network_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neural_network',
            name='description',
            field=models.TextField(default='Дефолтное описание', help_text='Максимальная 1000 символов', max_length=10000, verbose_name='Описание'),
        ),
    ]
