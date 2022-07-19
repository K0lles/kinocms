from django.forms import modelform_factory, modelformset_factory, BaseModelFormSet, ModelForm, fields
from cinema.models import *
from page.models import *


cinema_form_factory = modelform_factory(Cinema, fields='__all__')
photo_formset_factory = modelformset_factory(Photo, fields='__all__', extra=0)
seo_form_factory = modelform_factory(SEO, fields='__all__')


#
# class CinemaCreateForm(forms.ModelForm):
#     class Meta:
#         model = Cinema
#         exclude = ('seo',)


class PhotoCreateForm(BaseModelFormSet):
    class Meta:
        model = Photo
        fields = ('photo',)


class SeoCreateForm(ModelForm):
    class Meta:
        model = SEO
        fields = '__all__'


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'description']

    def meta(self):
        return self._meta
