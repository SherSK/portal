# Generated by Django 3.1.2 on 2020-11-25 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secapp', '0002_auto_20201125_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 25, 21, 31, 59, 236664), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
    ]
