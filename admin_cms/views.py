from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from .forms import *
from cinema.models import Cinema
from user.models import SimpleUser


def cinema_view(request):
    cinema_list = Cinema.objects.all()

    context = {
        'title': 'KinoCMS| Список кінотеатрів',
        'cinema_list': cinema_list,
        'curr_page': 'cinema'
    }
    return render(request, 'admin_cms/cinema.html', context=context)


def create_cinema(request):
    cinema_form = cinema_form_factory()
    photo_formset = photo_formset_factory(queryset=Photo.objects.none())
    seo_form = seo_form_factory()

    context = {
        'title': 'KinoCMS| Список кінотеатрів',
        'cinema_form': cinema_form,
        'photo_formset': photo_formset,
        'seo_form': seo_form,
        'curr_page': 'cinema'
    }

    if request.method == 'POST':
        photo_formset_class = photo_formset_factory(request.POST, request.FILES)
        cinema_form_class = cinema_form_factory(request.POST, request.FILES)
        seo_form_class = seo_form_factory(request.POST)

        if cinema_form_class.is_valid() and seo_form_class.is_valid() \
                and all([form.is_valid() for form in photo_formset_class]):

            # creating new Gallery object manually for usage in cinema_form_class
            new_gallery_object = Gallery.objects.create(name=request.POST['name'])
            new_gallery_object.save()
            new_seo_object = seo_form_class.save()

            # setting for Gallery and SEO field in Cinema gallery and seo created objects
            cinema = cinema_form_class.save(commit=False)
            cinema.gallery = new_gallery_object
            cinema.seo = new_seo_object

            # setting gallery object in gallery field for every photo_form_class
            for photo_form_class in photo_formset_class:
                photo = photo_form_class.save(commit=False)
                photo.gallery = new_gallery_object

            photo_formset_class.save()

            cinema.save()
            return redirect('cinema')

        context['cinema_form'] = cinema_form_class
        context['photo_formset'] = photo_formset_class
        context['seo_form'] = seo_form_class

    return render(request, 'admin_cms/cinema_form.html', context=context)


def update_cinema(request, pk):
    cinema = Cinema.objects.select_related('gallery', 'seo').prefetch_related('hall_set', 'gallery__photo_set').get(pk=pk)

    # cinema = Cinema.objects.get(pk=pk)
    # gallery = Gallery.objects.prefetch_related('photo_set').get(pk=cinema.gallery_id)
    # halls = Hall.objects.filter(cinema_id=cinema)
    #
    # cinema_form = cinema_form_factory(instance=cinema)
    # hall_formset = hall_formset_factory(queryset=halls, prefix='hall')
    # seo_form = seo_form_factory(instance=cinema.seo)
    # photo_formset = photo_formset_factory(queryset=gallery.photo_set.all())

    cinema_form = cinema_form_factory(instance=cinema)
    hall_formset = hall_formset_factory(queryset=cinema.hall_set.all(), prefix='hall')
    seo_form = seo_form_factory(instance=cinema.seo)
    photo_formset = photo_formset_factory(queryset=cinema.gallery.photo_set.all())

    # print(gallery.photo_set)
    # print(halls)

    context = {
        'cinema_form': cinema_form,
        'hall_formset': hall_formset,
        'photo_formset': photo_formset,
        'seo_form': seo_form,
        'curr_page': 'cinema'
    }

    if request.method == 'POST':
        # photo_formset_class = photo_formset_factory(request.POST, request.FILES, queryset=gallery.photo_set.all())
        # cinema_form_class = cinema_form_factory(request.POST, request.FILES, instance=cinema)
        # seo_form_class = seo_form_factory(request.POST, instance=cinema.seo)
        # hall_formset_class = hall_formset_factory(request.POST, queryset=halls, prefix='hall')
        photo_formset_class = photo_formset_factory(request.POST, request.FILES, queryset=cinema.gallery.photo_set.all())
        cinema_form_class = cinema_form_factory(request.POST, request.FILES, instance=cinema)
        seo_form_class = seo_form_factory(request.POST, instance=cinema.seo)
        hall_formset_class = hall_formset_factory(request.POST, queryset=cinema.hall_set.all(), prefix='hall')

        if cinema_form_class.is_valid() and seo_form_class.is_valid() and photo_formset_class.is_valid() \
                and hall_formset_class.is_valid() \
                and all([form.is_valid() for form in photo_formset_class]) \
                and all([deleted_form.is_valid() for deleted_form in hall_formset_class.deleted_forms]):

            for form in photo_formset_class:
                form_saved = form.save(commit=False)
                if form_saved.photo:
                    form_saved.gallery = cinema.gallery
                    form_saved.save()

            for deleted_form in hall_formset_class.deleted_forms:
                deleted_form_saved = deleted_form.save(commit=False)
                deleted_form_saved.gallery.delete()
                deleted_form_saved.seo.delete()

            cinema_form_class.save()
            photo_formset_class.save()
            seo_form_class.save()
            hall_formset_class.save()

            return redirect('cinema')

        context['cinema_form'] = cinema_form_class
        context['photo_formset'] = photo_formset_class
        context['seo_form'] = seo_form_class

    return render(request, 'admin_cms/cinema_change_form.html', context=context)


def delete_cinema(request, pk):
    try:
        cinema_to_delete = Cinema.objects.select_related('seo', 'gallery')\
            .prefetch_related('hall_set', 'hall_set__seo', 'hall_set__gallery').get(pk=pk)
        # cinema_to_delete = Cinema.objects.get(pk=pk)
        # halls = Hall.objects.filter(cinema_id=cinema_to_delete)

        # deleting all related objects to Cinema
        for hall in cinema_to_delete.hall_set.all():
            hall.seo.delete()
            hall.gallery.delete()
            hall.delete()

        cinema_to_delete.gallery.delete()
        cinema_to_delete.seo.delete()
        cinema_to_delete.delete()

    finally:
        return redirect('cinema')
        # cinema_list = Cinema.objects.all().values('id', 'name', 'logo')
        # context = {
        #     'cinema_list': cinema_list,
        #     'title': 'KinoCMS| Список кінотеатрів',
        #     'curr_page': 'cinema'
        # }
        #
        # return render(request, 'admin_cms/cinema.html', context=context)


def create_hall(request, cinema_pk):
    hall_form = hall_form_factory()
    photo_formset = photo_formset_factory(queryset=Photo.objects.none())
    seo_form = seo_form_factory()

    if request.method == 'POST':
        hall_form = hall_form_factory(request.POST, request.FILES or None)
        photo_formset = photo_formset_factory(request.POST, request.FILES or None)
        seo_form = seo_form_factory(request.POST)

        if hall_form.is_valid() and photo_formset.is_valid() and all([form.is_valid() for form in photo_formset]) \
                and seo_form.is_valid():

            gallery = Gallery.objects.create(name=f"Hall {request.POST['number']}")
            gallery.save()
            seo_object = seo_form.save()

            for form in photo_formset:
                photo = form.save(commit=False)
                photo.gallery = gallery

            hall_form_saved = hall_form.save(commit=False)
            hall_form_saved.gallery = gallery
            hall_form_saved.cinema_id = Cinema.objects.get(pk=cinema_pk)
            hall_form_saved.seo = seo_object
            hall_form_saved.save()
            photo_formset.save()

            return redirect('update_cinema', pk=cinema_pk)

    context = {
        'title': 'KinoCMS | Створення зала',
        'curr_page': 'cinema',
        'hall_form': hall_form,
        'photo_formset': photo_formset,
        'seo_form': seo_form,
        'cinema_id': cinema_pk
    }

    return render(request, 'admin_cms/hall_form.html', context=context)


def update_hall(request, hall_pk):
    # hall = Hall.objects.get(pk=hall_pk)
    # gallery = Gallery.objects.prefetch_related('photo_set').get(pk=hall.gallery.pk)
    hall = Hall.objects.select_related('seo', 'gallery').prefetch_related('gallery__photo_set').get(pk=hall_pk)
    hall_form = hall_form_factory(instance=hall)
    seo_form = seo_form_factory(instance=hall.seo)
    photo_formset = photo_formset_factory(queryset=hall.gallery.photo_set.all())

    context = {
        'hall_form': hall_form,
        'seo_form': seo_form,
        'photo_formset': photo_formset,
        'curr_page': 'cinema',
        'title': 'KinoCMS | Редагування залу'
    }

    if request.method == "POST":
        hall_form = hall_form_factory(request.POST, request.FILES, instance=hall)
        seo_form = seo_form_factory(request.POST, instance=hall.seo)
        # photo_formset = photo_formset_factory(request.POST, request.FILES, queryset=gallery.photo_set.all())
        photo_formset = photo_formset_factory(request.POST, request.FILES, queryset=hall.gallery.photo_set.all())

        if hall_form.is_valid() and seo_form.is_valid() and photo_formset.is_valid() \
                and all([form.is_valid() for form in photo_formset]):

            hall_saved = hall_form.save()
            seo_form.save()

            gallery_to_save = Gallery.objects.get(pk=hall.gallery.pk)
            gallery_to_save.name = f"Hall {hall_saved.number}"
            gallery_to_save.save()

            for form in photo_formset:
                photo = form.save(commit=False)
                if photo.photo:
                    photo.gallery = hall.gallery
                    photo.save()
            photo_formset.save()

            return redirect('update_cinema', pk=hall.cinema_id.pk)

        context['hall_form'] = hall_form
        context['seo_form'] = seo_form
        context['photo_formset'] = photo_formset

    return render(request, 'admin_cms/hall_change_form.html', context=context)


def movie_view(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }

    return render(request, 'admin_cms/movies.html', context=context)


def create_movie(request):
    movie_form = MovieForm()
    photo_formset = photo_formset_factory(queryset=Photo.objects.none())
    seo_form = seo_form_factory()

    context = {
        'title': 'KinoCMS | Створення фільму',
        'movie_form': movie_form,
        'photo_formset': photo_formset,
        'seo_form': seo_form
    }

    if request.method == 'POST':
        movie_form_class = MovieForm(request.POST, request.FILES or None)
        photo_formset_class = photo_formset_factory(request.POST, request.FILES or None)
        seo_form_class = seo_form_factory(request.POST)

        if movie_form_class.is_valid() and all([form.is_valid() for form in photo_formset_class]) \
                and seo_form_class.is_valid():
            new_gallery = Gallery.objects.create(name=movie_form_class.cleaned_data.get('name'))
            new_seo = seo_form_class.save()
            movie_saved = movie_form_class.save(commit=False)
            movie_saved.gallery = new_gallery
            movie_saved.seo = new_seo
            movie_saved.save()

            for photo in photo_formset_class:
                if photo.cleaned_data.get('photo'):
                    photo_saved = photo.save(commit=False)
                    photo_saved.gallery = new_gallery
                    photo_saved.save()

            return redirect('cinema')

        context['movie_form'] = movie_form_class
        context['photo_formset'] = photo_formset_class
        context['seo_form'] = seo_form_class

    return render(request, 'admin_cms/movie_form.html', context=context)


def update_movie(request, pk):
    # movie = Movie.objects.select_related('gallery', 'seo').get(pk=pk)
    movie = Movie.objects.select_related('gallery', 'seo').prefetch_related('gallery__photo_set').get(pk=pk)
    movie_form = MovieForm(instance=movie)
    seo_form = seo_form_factory(instance=movie.seo)
    photo_formset = photo_formset_factory(queryset=movie.gallery.photo_set.all())
    context = {
        'movie_form': movie_form,
        'photo_formset': photo_formset,
        'seo_form': seo_form
    }

    if request.method == 'POST':
        movie_form_class = MovieForm(request.POST, request.FILES, instance=movie)
        seo_form_class = seo_form_factory(request.POST, instance=movie.seo)
        photo_formset_class = photo_formset_factory(request.POST, request.FILES, queryset=movie.gallery.photo_set.all())

        if movie_form_class.is_valid() and seo_form_class.is_valid() and photo_formset_class.is_valid() \
                and all([form.is_valid() for form in photo_formset_class]) \
                and all([deleted_form.is_valid() for deleted_form in photo_formset_class.deleted_forms]):

            for form in photo_formset_class:
                form_saved = form.save(commit=False)
                if form_saved.photo:
                    form_saved.gallery = movie.gallery
                    form.save()

            photo_formset_class.save()
            seo_form_class.save()
            movie_form_class.save()
            return redirect('movie')

        context['movie_form'] = movie_form_class
        context['seo_form'] = seo_form_class
        context['photo_formset'] = photo_formset_class

    return render(request, 'admin_cms/movie_change_form.html', context=context)


def create_banner(request):
    main_top_banner_form = main_top_banner_form_factory()
    main_top_photo_formset = main_top_formset_factory(queryset=MainTopBannerPhoto.objects.none())
    background_banner_form = background_banner_form_factory()
    news_banner_form = news_banner_form_factory()
    news_banner_formset = news_banner_formset_factory(queryset=NewsBannerPhoto.objects.none(), prefix='news')

    context = {
        'main_top_banner_form': main_top_banner_form,
        'main_top_photo_formset': main_top_photo_formset,
        'background_banner_form': background_banner_form,
        'news_banner_form': news_banner_form,
        'news_banner_formset': news_banner_formset,
        'curr_page': 'banners',
        'title': 'KinoCMS | Створення банерів'
    }

    if request.method == 'POST':

        if 'main_top_banner' in request.POST:
            main_top_banner_form_class = main_top_banner_form_factory(request.POST, request.FILES or None)
            main_top_photo_formset_class = main_top_formset_factory(request.POST, request.FILES or None)

            if main_top_banner_form_class.is_valid() and main_top_photo_formset_class.is_valid() and \
                    all([form.is_valid() for form in main_top_photo_formset_class]):

                main_banner_saved = main_top_banner_form_class.save()

                for form in main_top_photo_formset_class:
                    if form.cleaned_data.get('photo') and form.cleaned_data.get('url') \
                            and form.cleaned_data.get('text'):
                        main_banner_photo_saved = form.save(commit=False)
                        main_banner_photo_saved.main_top_banner = main_banner_saved
                        main_banner_photo_saved.save()

                return redirect('create_banner')

            context['main_top_banner_form'] = main_top_banner_form_class
            context['main_top_photo_formset'] = main_top_photo_formset_class

        if 'background_banner' in request.POST:
            background_banner_form_class = background_banner_form_factory(request.POST, request.FILES or None)
            if background_banner_form_class.is_valid():
                background_banner_form_class.save()
                return redirect('create_banner')

            context['background_banner_form'] = background_banner_form_class

        if 'news_banner' in request.POST:
            news_banner_form_class = news_banner_form_factory(request.POST)
            news_banner_formset_class = news_banner_formset_factory(request.POST, request.FILES or None, prefix='news')

            if news_banner_form_class.is_valid() and news_banner_formset_class.is_valid() \
                    and all([form.is_valid() for form in news_banner_formset_class]):

                news_banner_saved = news_banner_form_class.save()

                for form in news_banner_formset_class:
                    if form.cleaned_data.get('photo') and form.cleaned_data.get('url'):
                        news_banner_photo_saved = form.save(commit=False)
                        news_banner_photo_saved.news_banner = news_banner_saved
                        news_banner_photo_saved.save()

                return redirect('create_banner')

            context['news_banner_form'] = news_banner_form_class
            context['news_banner_formset'] = news_banner_formset_class

    return render(request, 'admin_cms/banner_form.html', context=context)


def create_page(request):
    page_form = PageCreateForm()
    seo_form = seo_form_factory()
    photo_formset = photo_formset_factory(queryset=Photo.objects.none())

    context = {
        'form': page_form,
        'seo_form': seo_form,
        'photo_formset': photo_formset,
        'curr_page': 'pages',
        'title': 'KinoCMS | Створення сторінок'
    }

    if request.method == 'POST':
        page_form = PageCreateForm(request.POST)
        page_form.save(commit=False)

    return render(request, 'admin_cms/page_form.html', context=context)


def users(request):
    # if request.user.is_superuser:
    simple_users = SimpleUser.objects.all()
    paginator = Paginator(simple_users, 5)

    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    context = {
        'users': page_objects
    }
    return render(request, 'admin_cms/users.html', context=context)
    # return HttpResponseForbidden()


def user_update(request, pk):
    if request.user.is_superuser:
        try:
            simple_user_instance = SimpleUser.objects.get(pk=pk)
            simple_user = UserFormUpdate(instance=simple_user_instance)
            context = {
                'simple_user': simple_user,
                'title': 'KinoCMS | Редагування користувача'
            }
            if request.method == 'POST':
                simple_user_class = UserFormUpdate(request.POST, instance=simple_user_instance)
                if simple_user_class.is_valid():

                    # saving old password for occasion if new password not entered
                    old_password = SimpleUser.objects.get(email=simple_user_class.cleaned_data.get('email')).password

                    new_password = simple_user_class.cleaned_data.get('password')
                    user_saved = simple_user_class.save()
                    if new_password:
                        user = SimpleUser.objects.get(email=user_saved.email)
                        user.set_password(new_password)
                        user.save()

                    # if no password were entered, old password is set again
                    else:
                        user_saved.password = old_password
                        user_saved.save()
                    return redirect('users')
                context = {
                    'simple_user': simple_user_class,
                    'title': 'KinoCMS | Редагування користувача'
                }
                return render(request, 'admin_cms/user_change_form.html', context=context)

            return render(request, 'admin_cms/user_change_form.html', context=context)

        except:
            return redirect('users')

    return HttpResponseForbidden()


def user_delete(request, pk):
    if request.user.is_superuser:
        try:
            user_to_delete = SimpleUser.objects.get(pk=pk)
            user_to_delete.delete()
        finally:
            return redirect('users')
    return HttpResponseForbidden()
