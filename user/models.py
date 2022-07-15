from django.db import models
from django.contrib.auth.models import User
from movie.models import Session


class SimpleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, verbose_name='Імʼя')
    surname = models.CharField(max_length=55, verbose_name='Прізвище')
    alias = models.CharField(max_length=55, verbose_name='Псевдонім')
    email = models.EmailField(verbose_name='E-mail')
    password = models.CharField(max_length=55, verbose_name='Пароль')
    card_number = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Номер карти')

    class Language(models.TextChoices):
        UKRAINIAN = 'ukrainian', 'Українська'
        RUSSIAN = 'russian', 'Російська'

    language = models.CharField(choices=Language.choices, verbose_name='Мова')

    class Sex(models.TextChoices):
        MALE = 'male', 'Чоловік'
        FEMALE = 'female', 'Жінка'

    sex = models.IntegerField(choices=Sex.choices, verbose_name='Стать')
    phone_number = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Телефон')
    birthday = models.DateField(verbose_name='Дата народження')
    city = models.CharField(max_length=55, verbose_name='Місто')


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    row_number = models.IntegerField(verbose_name='Номер ряду')
    seat_number = models.IntegerField(verbose_name='Номер місця')
