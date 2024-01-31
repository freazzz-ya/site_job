# Generated by Django 5.0.1 on 2024-01-30 20:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_worker_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(choices=[('Карина', 'КАРИНА'), ('Максим', 'МАКСИМ'), ('Мы', 'МЫ')], max_length=256, verbose_name='Имя пользователя')),
                ('text', models.TextField(default='Данный пользователь ничего о себе не написал, но мы уверены, что это очень хороший и позитивный человек, который скоро добьется финансовых успехов.', max_length=256, verbose_name='Договоренность')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'Специальная модель',
                'verbose_name_plural': 'Специальные модели',
                'db_table': 'Special',
            },
        ),
    ]
