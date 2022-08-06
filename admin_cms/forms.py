from django.forms import modelform_factory, modelformset_factory, ModelForm
from django.forms.widgets import FileInput, Textarea, TextInput, CheckboxInput
from cinema.models import *
from page.models import *


photo_formset_factory = modelformset_factory(Photo, fields=('photo',), extra=0,
                                             widgets={
                                                 'photo': FileInput(attrs={'onchange': 'loadFile(event, this.id)',
                                                                           'accept': 'image/*'}),
                                             },
                                             can_delete=True)


cinema_form_factory = modelform_factory(Cinema, exclude=('gallery', 'seo'),
                                        widgets={
                                            'name': TextInput(attrs={'class': 'form-control'}),
                                            'description': Textarea(attrs={'class': 'form-control'}),
                                            'condition': Textarea(attrs={'class': 'form-control'}),
                                            'logo': FileInput(attrs={'onchange': 'loadFile(event, this.id)'}),
                                            'banner_photo': FileInput(attrs={'onchange': 'loadFile(event, this.id)'})
                                        })


seo_form_factory = modelform_factory(SEO, fields=('url', 'title', 'keyword', 'seo_description'),
                                     widgets={
                                         'url': TextInput(attrs={'class': 'form-control'}),
                                         'title': TextInput(attrs={'class': 'form-control'}),
                                         'keyword': TextInput(attrs={'class': 'form-control'}),
                                         'seo_description': Textarea(attrs={'class': 'form-control'})
                                     })

hall_form_factory = modelform_factory(Hall, exclude=('gallery', 'created_at', 'row_amount', 'seat_amount'))


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('gallery', 'seo',)
