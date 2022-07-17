from django.shortcuts import render
from django.views.generic import CreateView

from cinema.models import Cinema


class CinemaCreateView(CreateView):
    model = Cinema
    fields = ('name', 'description', 'condition', 'logo')
    template_name = 'admin_cms/base.html'
