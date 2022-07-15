from django.db import models
from cinema.models import Gallery, SEO


class MainPage(models.Model):
    phone_number_first = models.DecimalField(max_digits=10, decimal_places=0)
    phone_number_second = models.DecimalField(max_digits=10, decimal_places=0)
    seo_text = models.TextField(verbose_name='SEO текст')
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)


class Page(models.Model):
    name = models.CharField(max_length=55, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    main_photo = models.ImageField(upload_to='page/', verbose_name='Головна картинка')
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, verbose_name='Галерея картинок')
    status = models.BooleanField(default=True)
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE)
