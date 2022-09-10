from django.shortcuts import render
from banner.models import *
from movie.models import *
from page.models import *


def header_data(request):
    """Returns data, which will be in the header on each user page"""
    main_page = MainPage.objects.first()
    return {
        'phone_number_first': main_page.phone_number_first if main_page.phone_number_first else '+380500000000',
        'phone_number_second': main_page.phone_number_second if main_page.phone_number_second else '+380500000000',
        'admin': True if (request.user.is_authenticated and request.user.is_superuser) else False,
        'authenticated': False if request.user.is_anonymous else True
        }


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
    }

    # there and further - adding keys with phone numbers
    context.update(header_data(request))

    return render(request, 'cinema/home.html', context=context)


def poster_view(request):
    movies = Movie.objects.filter(session__date__month__gte=timezone.now().month)

    context = {
        'title': 'KinoCMS | Афіша',
        'movies': movies,
    }
    context.update(header_data(request))

    return render(request, 'cinema/poster.html', context=context)


def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    print(movie)

    return render(request, '', )
