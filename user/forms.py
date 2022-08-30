from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, Form, EmailField
from django.forms.widgets import RadioSelect, NumberInput, TextInput, PasswordInput
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class UserRegistrationForm(UserCreationForm):

    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторіть пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sex'].empty_label = None
        self.fields['birthday'].input_formats = [ '%d-%m-%Y' ]
        del self.fields['password2']

    class Meta:
        model = SimpleUser
        exclude = ['date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше ім'я", 'value': ''}),
            'surname': TextInput(attrs={'class': 'form-control', 'placeholder': "Ваше прізвище"}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': "E-mail"}),
            'alias': TextInput(attrs={'class': 'form-control', 'placeholder': "Псевдонім"}),
            'birthday': TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата народження'}),
            'phone_number': PhoneNumberInternationalFallbackWidget(attrs={'class': 'form-control', 'placeholder': 'Номер телефону'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': "Місто"}),
            'card_number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Номер банківської картки'}),
            'language': RadioSelect(attrs={'class': 'form-check-input'}),
            'sex': RadioSelect(attrs={'class': 'form-check-input'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введіть пароль'})
        }

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password1')

        if password != confirm_password:
            self.add_error('password', 'Passwords must match. Check it writing!')

        return cleaned_data

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(Form):
    email = EmailField(max_length=200, widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    password = CharField(max_length=200, widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
