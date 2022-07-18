from django.shortcuts import render
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
    cinema_form = CinemaCreateForm()
    photo_formset = modelformset_factory(Photo, formset=PhotoCreateForm, extra=0, fields=('photo',),
                                         labels={'photo': ''})
    seo_form = modelformset_factory(SEO, form=SeoCreateForm, extra=1)

    if request.method == 'POST':
        formset_class = photo_formset(request.POST, request.FILES)
        cinema_form = CinemaCreateForm(request.POST, request.FILES)
        seo_form_class = seo_form(request.POST)

        if cinema_form.is_valid() and seo_form_class.is_valid() and all(form.is_valid() for form in formset_class):
            seo_form_class.save()
            formset_class.save()
            cinema_form.save()

    context = {
        'title': 'KinoCMS| Список кінотеатрів',
        'form': cinema_form,
        'photo_formset': photo_formset(),
        'seo_form': seo_form(),
        'curr_page': 'cinema'
    }
    return render(request, 'admin_cms/cinema_form.html', context=context)
