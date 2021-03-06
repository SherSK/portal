# Generated by Django 3.1.2 on 2020-11-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(choices=[('1', 'Первый'), ('2', 'Второй'), ('3', 'Третий'), ('4', 'Четвертый')], default='Выбор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
    ]
