from django.db import models
class Kani(models.Model):
    content = models.TextField(blank=True, verbose_name='цитата')
    razbor=models.TextField(blank=True, verbose_name='разбор')


# Create your models here.
