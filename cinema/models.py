from django.db import models
from django.core.validators import MinValueValidator


class Cinema(models.Model):
    name = models.CharField(max_length=55, verbose_name='Назва кінотеатру')
    description = models.TextField(verbose_name='Опис')
    condition = models.TextField(verbose_name='Умови')
    logo = models.ImageField(upload_to='cinema/cinema/logo/', verbose_name='Логотип')
    banner_photo = models.ImageField(upload_to='cinema/cinema/banner_photo/', verbose_name='Фото верхнього баннера')
    gallery = models.OneToOneField('Gallery', on_delete=models.CASCADE, verbose_name='Галерея картинок')
    seo = models.ForeignKey('SEO', on_delete=models.CASCADE, verbose_name='SEO блок')


class Hall(models.Model):
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE, verbose_name='Кінотеатр')
    number = models.IntegerField(verbose_name='Номер зала')
    created_at = models.DateField(auto_now_add=True)
    scheme = models.ImageField(upload_to='cinema/hall/scheme/', verbose_name='Схема зала')
    banner_photo = models.ImageField(upload_to='cinema/hall/banner_photo/' ,verbose_name='Верхній баннер')
    gallery = models.OneToOneField('Gallery', on_delete=models.CASCADE, verbose_name='Галерея картинок')
    row_amount = models.IntegerField(default=6, validators=[MinValueValidator(1)])
    seat_amount = models.IntegerField(default=12, validators=[MinValueValidator(1)])
    seo = models.ForeignKey('SEO', on_delete=models.CASCADE, verbose_name='SEO блок')


class Gallery(models.Model):
    name = models.CharField(max_length=55)


class Photo(models.Model):
    photo = models.ImageField(upload_to='gallery/')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class SEO(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=55)
    keyword = models.CharField(max_length=155)
    description = models.TextField()
