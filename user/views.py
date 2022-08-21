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
            redirect('cinema_create')

    else:
        registration_form = UserRegistrationForm()

    context = {
        'registration_form': registration_form
    }
    return render(request, 'user/registration.html', context=context)


def login_in(request):
    if request.method == 'POST':
        login_form_class = UserLoginForm(request.POST)
        print(login_form_class.errors)

        if login_form_class.is_valid():
            email = login_form_class.cleaned_data['email']
            print(email)
            password = login_form_class.cleaned_data['password']
            print(password)
            user = authenticate(email=email, password=password)
            print(user)

            if user is not None and user.is_active:
                login(request, user)
                redirect('cinema')

    if request.user.is_anonymous:
        print(request.user)
        login_form = UserLoginForm()

        context = {
            'login_form': login_form
        }
        return render(request, 'user/login.html', context=context)

    return redirect('cinema')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
