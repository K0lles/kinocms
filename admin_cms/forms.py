from django.forms import modelform_factory, modelformset_factory, BaseForm, ModelForm, Form, fields
from django.forms.widgets import FileInput, Textarea, TextInput
from cinema.models import *
from page.models import *


photo_formset_factory = modelformset_factory(Photo, fields=('photo',), extra=0)


cinema_form_factory = modelform_factory(Cinema, exclude=('gallery', 'seo'),
                                        widgets={
                                            'name': TextInput(attrs={'class': 'form-control'}),
                                            'description': Textarea(attrs={'class': 'form-control'}),
                                            'condition': Textarea(attrs={'class': 'form-control'})
                                        })


seo_form_factory = modelform_factory(SEO, fields=('url', 'title', 'keyword', 'seo_description'),
                                     widgets={
                                         'url': TextInput(attrs={'class': 'form-control'}),
                                         'title': TextInput(attrs={'class': 'form-control'}),
                                         'keyword': TextInput(attrs={'class': 'form-control'}),
                                         'seo_description': Textarea(attrs={'class': 'form-control'})
                                     })


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('gallery', 'seo',)
