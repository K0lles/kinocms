from django.shortcuts import render
from banner.models import *
from movie.models import *
from django.utils import timezone
from datetime import datetime


def header_data():
    """Returns data, which will be in the header on each user page"""
    pass


def home_view(request):
    background_banner = BackgroundBanner.objects.first()
    main_top_banner_photos = MainTopBanner.objects.prefetch_related('maintopbannerphoto_set').first()
    sessions = Session.objects.prefetch_related('movie', 'hall').filter(date__month=timezone.now().month)

    context = {
        'title': 'KinoCMS | Головна',
        'background': background_banner.photo.url if background_banner.background == 1 else None,
        'photos': main_top_banner_photos.maintopbannerphoto_set.all(),
        'interval': main_top_banner_photos.turning_speed * 1000,
        'sessions': sessions,
        'admin': True if (request.user.is_authenticated and request.user.is_superuser) else False
    }

    return render(request, 'cinema/home.html', context=context)
