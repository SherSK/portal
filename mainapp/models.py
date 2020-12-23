from django.db import models
from pathlib import Path


class Category(models.Model):

    name=models.CharField(max_length=255,verbose_name='Имя ...')
    slug=models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Product(models.Model):

    Loan=(
        ('1','Первый'),
        ('2','Второй'),
        ('3','Третий'),
        ('4','Четвертый')
    )
    APP_DIR = Path(__file__).resolve().parent
    category=models.ForeignKey(Category, verbose_name=("Категория"), on_delete=models.CASCADE)
    slug=models.CharField(max_length=255,verbose_name='Наименование')
    image=models.ImageField(verbose_name='Изображение',upload_to=str(APP_DIR)+'/Pictures')
    description=models.TextField(choices=Loan,default='Выбор')

    def __str__(self):
        return f"{self.slug}({self.category})"
    

    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукты'