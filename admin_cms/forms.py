from django import forms
from cinema.models import *


class CinemaCreateForm(forms.ModelForm):
    class Meta:
        model = Cinema
        exclude = ('seo',)


class PhotoCreateForm(forms.BaseModelFormSet):
    class Meta:
        model = Photo
        fields = ('photo',)


class SeoCreateForm(forms.ModelForm):
    class Meta:
        model = SEO
        fields = '__all__'
