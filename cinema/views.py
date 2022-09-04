from django.shortcuts import render
from banner.models import *


def home_view(request):
    background_banner = BackgroundBanner.objects.first()

    context = {
        'background': background_banner.photo.url if background_banner.background == 1 else None
    }

    return render(request, 'cinema/home.html', context=context)
