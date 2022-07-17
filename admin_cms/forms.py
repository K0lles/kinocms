from django import forms
from cinema.models import *


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo',)


class CinemaCreateForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('name', 'logo')
