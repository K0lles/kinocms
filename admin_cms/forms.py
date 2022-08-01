from fileinput import FileInput

from django.forms import modelform_factory, modelformset_factory, BaseForm, ModelForm, Form, fields
from django.forms.widgets import FileInput
from cinema.models import *
from page.models import *


photo_formset_factory = modelformset_factory(Photo, fields=('photo',), extra=0)


class CinemaCreateForm(ModelForm):
    class Meta:
        exclude = ('gallery', 'seo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


cinema_form_factory = modelform_factory(Cinema, form=CinemaCreateForm)


class SeoCreateForm(ModelForm):
    class Meta:
        model = SEO
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


seo_form_factory = modelform_factory(SEO, form=SeoCreateForm)


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('gallery', 'seo',)
