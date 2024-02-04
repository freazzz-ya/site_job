# Generated by Django 5.0.1 on 2024-02-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_earning_scheme_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maling_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(error_messages={'unique': 'email существует уже'}, max_length=254, unique=True, verbose_name='Майл')),
            ],
            options={
                'verbose_name': 'Модель рассылки',
                'verbose_name_plural': 'Модели рассылки',
                'db_table': 'Maling_model',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Сontacts_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('email', models.EmailField(error_messages={'unique': 'email существует уже'}, max_length=254, unique=True, verbose_name='Майл')),
                ('discription', models.TextField(default='Дефолтное описание', max_length=10000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель контактов',
                'verbose_name_plural': 'Модели контактов',
                'db_table': 'Сontacts_model',
                'ordering': ('id',),
            },
        ),
    ]
