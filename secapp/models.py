from django.db import models
from django.urls import reverse
from django.utils.timezone import now

class Test(models.Model):

    name=models.CharField(max_length=255,verbose_name='Имя') 
    date=models.DateField(verbose_name='Дата',default=now)   

    class Meta:
        verbose_name = ("Событие")
        verbose_name_plural = ("События")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("test_detail", kwargs={"pk": self.pk})

