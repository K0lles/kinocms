from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import *


def registration(request):

    if request.method == 'POST':
        registration_form_class = UserRegistrationForm(request.POST)

        if registration_form_class.is_valid():
            registration_form_class.save()
            email = registration_form_class.cleaned_data.get('email')
            password = registration_form_class.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('cinema')

        context = {
            'registration_form': registration_form_class
        }

        return render(request, 'user/registration.html', context=context)

    registration_form = UserRegistrationForm()

    context = {
        'registration_form': registration_form
    }
    return render(request, 'user/registration.html', context=context)


def login_in(request):
    if request.method == 'POST':
        login_form_class = UserLoginForm(request.POST)

        if login_form_class.is_valid():
            email = login_form_class.cleaned_data['email']
            password = login_form_class.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect('cinema')

            login_form_class.add_error('password', 'Password is wrong, check the writing!')

        context = {
            'login_form': login_form_class
        }

        return render(request, 'user/login.html', context=context)

    if request.user.is_anonymous:
        login_form = UserLoginForm()

        context = {
            'login_form': login_form
        }
        return render(request, 'user/login.html', context=context)

    return redirect('cinema')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
