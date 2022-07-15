from django.db import models


class MainTopBanner(models.Model):

    class Speed(models.IntegerChoices):
        FIVE_SEC = 5, '5с'
        TEN_SEC = 10, '10с'
        FIFTEEN_SEC = 15, '15с'

    turning_speed = models.IntegerField(choices=Speed.choices)
    turned_on = models.BooleanField(default=True)


class MainTopBannerPhoto(models.Model):
    main_top_banner = models.ForeignKey(MainTopBanner, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='banner/main_top_banner/')
    url = models.URLField()
    text = models.TextField()


class NewsBanner(models.Model):

    class Speed(models.IntegerChoices):
        FIVE_SEC = 5, '5с'
        TEN_SEC = 10, '10с'
        FIFTEEN_SEC = 15, '15с'

    turning_speed = models.IntegerField(choices=Speed.choices)
    turned_on = models.BooleanField(default=True)


class NewsBannerPhoto(models.Model):
    news_banner = models.ForeignKey(NewsBanner, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='banner/news_banner/')
    url = models.URLField()


class BackgroundBanner(models.Model):
    photo = models.ImageField(upload_to='banner/background_banner/')

    class Type(models.IntegerChoices):
        PHOTO_BACKGROUND = 1, 'Фото на фон'
        BACKGROUND = 2, 'Просто фон'

    background = models.IntegerField(choices=Type.choices)
