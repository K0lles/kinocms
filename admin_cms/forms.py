from django.forms import modelform_factory, modelformset_factory, ModelForm, CharField
from django.forms.widgets import FileInput, Textarea, TextInput, Select, DateInput, DateTimeInput, NumberInput, \
    RadioSelect, PasswordInput
from user.models import SimpleUser
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


user_form_factory = modelform_factory(SimpleUser,
                                      fields='__all__',
                                      widgets={
                                          'name': TextInput(attrs={'class': 'form-control'}),
                                          'surname': TextInput(attrs={'class': 'form-control'}),
                                          'alias': TextInput(attrs={'class': 'form-control'}),
                                          'birthday': TextInput(attrs={'class': 'form-control',
                                                                       'placeholder': 'Дата народження'}),
                                          'phone_number': TextInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'Номер телефону'}),
                                          'card_number': NumberInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Номер банківської картки'}),
                                          'language': RadioSelect(attrs={'class': 'form-check-input'}),
                                          'sex': RadioSelect(attrs={'class': 'form-check-input'}),
                                          'city': TextInput(attrs={'class': 'form-control'}),
                                          'password1': PasswordInput(attrs={'class': 'form-control'})
                                      })


class UserFormUpdate(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sex'].empty_label = None
        self.fields['birthday'].input_formats = [ '%d.%m.%Y' ]
        self.fields['password'].required = False
        # del self.fields['password1']

    password_repeat = CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Новий пароль'}), required=False)

    class Meta:
        model = SimpleUser
        exclude = ['date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'alias': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'birthday': TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'Дата народження'}),
            'phone_number': TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Номер телефону'}),
            'card_number': NumberInput(attrs={'class': 'form-control',
                                              'placeholder': 'Номер банківської картки'}),
            'language': RadioSelect(attrs={'class': 'form-check-input'}),
            'sex': RadioSelect(attrs={'class': 'form-check-input'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Новий пароль'}),
        }

    def clean(self):
        cleaned_data = super(UserFormUpdate, self).clean()
        print('you are inside clean def')

        if cleaned_data.get('password') != cleaned_data.get('password_repeat') and cleaned_data.get('password'):
            self.add_error('password', "Passwords must match. Check the validity of entered passwords!")

        return cleaned_data


class PageCreateForm(ModelForm):
    class Meta:
        model = Page
        exclude = ('gallery', 'seo',)
