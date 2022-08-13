from django.forms import modelform_factory, modelformset_factory, ModelForm
from django.forms.widgets import FileInput, Textarea, TextInput, Select, DateTimeInput
from cinema.models import *
from page.models import *
from banner.models import *


hall_formset_factory = modelformset_factory(Hall, fields=('number', 'created_at'), extra=0,
                                            widgets={
                                               'number': TextInput(attrs={'readonly': True}),
                                               'created_at': DateTimeInput(attrs={'readonly': True})
                                            }, can_delete=True)

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

hall_form_factory = modelform_factory(Hall, exclude=('cinema_id', 'gallery', 'created_at', 'row_amount',
                                                     'seat_amount', 'seo'),
                                      widgets={
                                          'number': TextInput(attrs={'class': 'form-control'}),
                                          'description': Textarea(attrs={'class': 'form-control'}),
                                          'scheme': FileInput(attrs={'onchange': 'loadFile(event, this.id)'}),
                                          'banner_photo': FileInput(attrs={'onchange': 'loadFile(event, this.id)'})
                                      })

main_top_banner_form_factory = modelform_factory(MainTopBanner, fields=('turned_on', 'turning_speed'),
                                                 widgets={
                                                     'turning_speed': Select(attrs={'class': 'form-control'})
                                                 })

main_top_formset_factory = modelformset_factory(MainTopBannerPhoto, exclude=('main_top_banner',), extra=0,
                                                widgets={
                                                    'url': TextInput(attrs={'class': 'form-control'}),
                                                    'text': Textarea(attrs={'class': 'form-control'})
                                                }, can_delete=True)

news_banner_form_factory = modelform_factory(NewsBanner, fields=('turning_speed', 'turned_on'),
                                             widgets={
                                                 'turning_speed': Select(attrs={'class': 'form-control'})
                                             })

background_banner_form_factory = modelform_factory(BackgroundBanner, fields=('photo', 'background'),
                                                   widgets={
                                                       'background': Select(attrs={'class': 'form-control'})
                                                   })


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('gallery', 'seo',)
