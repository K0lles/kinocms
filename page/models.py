from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from cinema.models import Gallery, SEO


class MainPage(models.Model):
    phone_number_first = PhoneNumberField(verbose_name='Телефон')
    phone_number_second = PhoneNumberField()
    created_at = models.DateField(default=timezone.now, verbose_name='Дата створення')
    status = models.BooleanField(default=True)
    seo_text = models.TextField(verbose_name='SEO текст')
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE, blank=True, null=True)


class Page(models.Model):
    name = models.CharField(max_length=55, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    main_photo = models.ImageField(upload_to='page/', verbose_name='Головна картинка')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата створення')
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, verbose_name='Галерея картинок', blank=True,
                                   null=True)
    status = models.BooleanField(default=True)
    seo = models.OneToOneField(SEO, on_delete=models.CASCADE, blank=True, null=True)
