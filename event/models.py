from django.db import models
from cinema.models import Gallery, SEO


class Event(models.Model):
    name = models.CharField(max_length=55, verbose_name='Назва')
    date = models.DateField(auto_now_add=True, verbose_name='Дата публікації')
    description = models.TextField(verbose_name='Опис')
    logo = models.ImageField(upload_to='event/logo/', verbose_name='Головна картинка')
    gallery = models.ForeignKey(Gallery, verbose_name='Галерея картинок', on_delete=models.CASCADE)
    url = models.URLField(verbose_name='Посилання на відео')
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
