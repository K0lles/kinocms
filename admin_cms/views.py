from django.shortcuts import render, redirect
from django.forms import modelformset_factory, modelform_factory
from .forms import *

from cinema.models import Cinema, SEO


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
    cinema_form = cinema_form_factory(instance=cinema)
    seo_form = seo_form_factory(instance=cinema.seo)
    photo_formset = photo_formset_factory(queryset=gallery.photo_set.all())

    if request.method == 'POST':
        photo_formset_class = photo_formset_factory(request.POST, request.FILES,
                                                    queryset=gallery.photo_set.all())
        cinema_form_class = cinema_form_factory(request.POST, request.FILES, instance=cinema)
        seo_form_class = seo_form_factory(request.POST, instance=cinema.seo)

        print(photo_formset_class.errors)

        if cinema_form_class.is_valid() and seo_form_class.is_valid() and photo_formset_class.is_valid()\
                and all([form.is_valid() for form in photo_formset_class.extra_forms]):

            print('validated is successfully done')

            print(photo_formset_class.deleted_forms)

            for extra_form in photo_formset_class.extra_forms:
                extra_form_saved = extra_form.save(commit=False)
                extra_form_saved.gallery = gallery
                extra_form_saved.save()

            cinema_form_class.save()
            photo_formset_class.save()
            seo_form_class.save()

        return redirect('cinema')

    context = {
        'cinema_form': cinema_form,
        'photo_formset': photo_formset,
        'seo_form': seo_form,
        'curr_page': 'cinema'
    }
    return render(request, 'admin_cms/cinema_change_form.html', context=context)


def create_hall(request):
    pass


def create_page(request):
    page_form = PageCreateForm()
    seo_form = seo_form_factory()
    photo_formset = photo_formset_factory(queryset=Photo.objects.none())

    context = {
        'form': page_form
    }

    if request.method == 'POST':
        page_form = PageCreateForm(request.POST)
        page_form.save(commit=False)

    return render(request, 'admin_cms/page_form.html', context=context)
