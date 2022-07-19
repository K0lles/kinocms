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
    # cinema_form = CinemaCreateForm()
    # photo_formset = modelformset_factory(Photo, formset=PhotoCreateForm, extra=0, fields=('photo',),
    #                                      labels={'photo': ''})
    # seo_form = modelformset_factory(SEO, form=SeoCreateForm, extra=1)
    cinema_form = cinema_form_factory()
    photo_formset = photo_formset_factory()
    seo_form = seo_form_factory()

    context = {
        'title': 'KinoCMS| Список кінотеатрів',
        'form': cinema_form,
        'photo_formset': photo_formset,
        'seo_form': seo_form,
        'curr_page': 'cinema'
    }

    if request.method == 'POST':
        photo_formset_class = photo_formset_factory(request.POST, request.FILES)
        cinema_form_class = cinema_form_factory(request.POST, request.FILES)
        seo_form_class = seo_form_factory(request.POST)
        len(photo_formset_class)

        if cinema_form_class.is_valid():
            print('cinema validation')

        if seo_form_class.is_valid():
            print("seo validation")

        for form in photo_formset_class:
            print(form.data)

        if cinema_form_class.is_valid() and seo_form_class.is_valid() \
                and all([form.is_valid() for form in photo_formset_class]):

            print("Yes, validation was completely upgraded")

            # creating new Gallery object manually for usage in cinema_form_class
            new_gallery_object = Gallery.objects.create(name=request.POST['name'])
            new_gallery_object.save()
            new_seo_object = seo_form_class.save()

            # setting for Gallery and SEO field in Cinema gallery and seo created objects

            cinema = cinema_form_class.save()
            cinema.gallery = new_gallery_object
            cinema.seo = new_seo_object
            cinema.save()

            print(len(photo_formset))
            # checking if there are any photos in photo_formset_class
            for photo_form_class in photo_formset_class:
                # setting gallery object in gallery field for every photo_form_class
                photo_form_class.fields['gallery'] = new_gallery_object
                photo = photo_form_class.save()
                print(photo.id, photo.gallery.id)
                photo.gallery = new_gallery_object
                # print("---------------------")
                # print(photo_form_class.fields)

            # photo_form_class.save()

            cinema.save()
            return redirect('cinema')

    return render(request, 'admin_cms/cinema_form.html', context=context)


def create_page(request):
    page_form = PageCreateForm()
    context = {
        'form': page_form
    }

    if request.method == 'POST':
        page_form = PageCreateForm(request.POST)
        print(page_form.fields['name'], page_form.fields['description'])
        print("-----------------")
        print(request.POST)
        # page_form.save(commit=False)

    return render(request, 'admin_cms/page_form.html', context=context)
