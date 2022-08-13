from django.shortcuts import render, redirect
from .forms import *

from cinema.models import Cinema


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

    return render(request, 'admin_cms/cinema_form.html', context=context)


def update_cinema(request, pk):
    cinema = Cinema.objects.get(pk=pk)
    gallery = Gallery.objects.prefetch_related('photo_set').get(pk=cinema.gallery_id)
    halls = Hall.objects.filter(cinema_id=cinema)

    if request.method == 'POST':
        photo_formset_class = photo_formset_factory(request.POST, request.FILES, queryset=gallery.photo_set.all())
        cinema_form_class = cinema_form_factory(request.POST, request.FILES, instance=cinema)
        seo_form_class = seo_form_factory(request.POST, instance=cinema.seo)
        hall_formset_class = hall_formset_factory(request.POST, queryset=halls, prefix='hall')

        if cinema_form_class.is_valid() and seo_form_class.is_valid() and photo_formset_class.is_valid() \
                and hall_formset_class.is_valid() \
                and all([form.is_valid() for form in photo_formset_class.extra_forms]) \
                and all([deleted_form.is_valid() for deleted_form in hall_formset_class.deleted_forms]):

            for form in photo_formset_class:
                form_saved = form.save(commit=False)
                form_saved.gallery = gallery
                form_saved.save()

            for deleted_form in hall_formset_class.deleted_forms:
                deleted_form_saved = deleted_form.save(commit=False)
                deleted_form_saved.gallery.delete().save()
                deleted_form_saved.seo.delete().save()
                deleted_form_saved.save()

            cinema_form_class.save()
            photo_formset_class.save()
            seo_form_class.save()
            hall_formset_class.save()

        return redirect('cinema')

    else:
        cinema_form = cinema_form_factory(instance=cinema)
        hall_formset = hall_formset_factory(queryset=halls, prefix='hall')
        seo_form = seo_form_factory(instance=cinema.seo)
        photo_formset = photo_formset_factory(queryset=gallery.photo_set.all())

    context = {
        'cinema_form': cinema_form,
        'hall_formset': hall_formset,
        'photo_formset': photo_formset,
        'seo_form': seo_form,
        'curr_page': 'cinema'
    }
    return render(request, 'admin_cms/cinema_change_form.html', context=context)


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
    hall = Hall.objects.get(pk=hall_pk)
    gallery = Gallery.objects.prefetch_related('photo_set').get(pk=hall.gallery.pk)

    hall_form = hall_form_factory(instance=hall)
    seo_form = seo_form_factory(instance=hall.seo)
    photo_formset = photo_formset_factory(queryset=gallery.photo_set.all())

    if request.method == "POST":
        hall_form = hall_form_factory(request.POST, request.FILES, instance=hall)
        seo_form = seo_form_factory(request.POST, instance=hall.seo)
        photo_formset = photo_formset_factory(request.POST, request.FILES, queryset=gallery.photo_set.all())

        if hall_form.is_valid() and seo_form.is_valid():
            hall_form.save()
            seo_form.save()

        if photo_formset.is_valid() and all([form.is_valid() for form in photo_formset]):

            for form in photo_formset:
                photo = form.save(commit=False)
                photo.gallery = hall.gallery
                photo.save()
            photo_formset.save()

        return redirect('update_cinema', pk=hall.cinema_id.pk)

    context = {
        'hall_form': hall_form,
        'seo_form': seo_form,
        'photo_formset': photo_formset,
        'curr_page': 'cinema',
        'title': 'KinoCMS | Редагування залу'
    }

    return render(request, 'admin_cms/hall_change_form.html', context=context)


def create_banner(request):
    main_top_banner_form = main_top_banner_form_factory()
    main_top_photo_formset = main_top_formset_factory(queryset=MainTopBannerPhoto.objects.none())
    background_banner_form = background_banner_form_factory()
    news_banner_form = news_banner_form_factory()

    context = {
        'main_top_banner_form': main_top_banner_form,
        'main_top_photo_formset': main_top_photo_formset,
        'background_banner_form': background_banner_form,
        'news_banner_form': news_banner_form,
        'curr_page': 'banners',
        'title': 'KinoCMS | Створення банерів'
    }

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
