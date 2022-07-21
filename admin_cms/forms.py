from django.forms import modelform_factory, modelformset_factory, BaseForm, ModelForm, fields
from cinema.models import *
from page.models import *


cinema_form_factory = modelform_factory(Cinema, exclude=('gallery', 'seo'))
photo_formset_factory = modelformset_factory(Photo, fields=('photo',), extra=3)
seo_form_factory = modelform_factory(SEO, fields='__all__')


#
# class CinemaCreateForm(forms.ModelForm):
#     class Meta:
#         model = Cinema
#         exclude = ('seo',)


class PhotoCreateForm(BaseForm):
    pass


class SeoCreateForm(ModelForm):
    class Meta:
        model = SEO
        fields = '__all__'


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('gallery', 'seo',)
