from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from movie.models import Session


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_admin', True)
        kwargs.setdefault('is_superuser', True)

        return self.create_user(email, password, **kwargs)


class SimpleUser(AbstractBaseUser):

    name = models.CharField(max_length=55, verbose_name='Імʼя')
    surname = models.CharField(max_length=55, verbose_name='Прізвище')
    alias = models.CharField(max_length=55, verbose_name='Псевдонім', unique=True)
    email = models.EmailField(verbose_name='E-mail', unique=True)
    password = models.CharField(max_length=55, verbose_name='Пароль')
    card_number = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Номер карти')

    class Language(models.TextChoices):
        UKRAINIAN = 'ukrainian', 'Українська'
        RUSSIAN = 'russian', 'Російська'

    language = models.CharField(max_length= 55, choices=Language.choices, verbose_name='Мова')

    class Sex(models.TextChoices):
        MALE = 'male', 'Чоловік'
        FEMALE = 'female', 'Жінка'

    sex = models.IntegerField(choices=Sex.choices, verbose_name='Стать')
    phone_number = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Телефон')
    birthday = models.DateField(verbose_name='Дата народження')
    city = models.CharField(max_length=55, verbose_name='Місто')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['email', 'password']


class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    row_number = models.IntegerField(verbose_name='Номер ряду')
    seat_number = models.IntegerField(verbose_name='Номер місця')
