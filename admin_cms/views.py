from django.shortcuts import render
from django.forms import modelformset_factory
from .forms import *

from cinema.models import Cinema, SEO


def create_cinema(request):
    cinema_form = CinemaCreateForm()
    photo_form_set = modelformset_factory(Photo, form=PhotoCreateForm, extra=2)

    return render(request, 'admin_cms/cinema_form.html', context={'form': cinema_form,
                                                                  'photo_form': photo_form_set})


# class CinemaCreateView(CreateView):
#     form_class = CinemaCreateForm
#     template_name = 'admin_cms/base.html'

