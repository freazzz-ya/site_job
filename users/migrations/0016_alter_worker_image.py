# Generated by Django 5.0.1 on 2024-01-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_worker_balance_alter_worker_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='image',
            field=models.ImageField(default='/static/images/nou.jpg', upload_to='images', verbose_name='image'),
        ),
    ]
