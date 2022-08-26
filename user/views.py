from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import *


def registration(request):

    if request.method == 'POST':
        registration_form_class = UserRegistrationForm(request.POST)
<<<<<<< HEAD
        print(registration_form_class.errors)

        if registration_form_class.is_valid():
            print('validation completed')
=======

        if registration_form_class.is_valid():
>>>>>>> 630369c3e2e9a552c8ca6173ec21b3061412630d
            registration_form_class.save()
            email = registration_form_class.cleaned_data.get('email')
            password = registration_form_class.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            login(request, user)
<<<<<<< HEAD
            return redirect('cinema')

        context = {
            'registration_form': registration_form_class
        }

        return render(request, 'user/registration.html', context=context)

    registration_form = UserRegistrationForm()
=======
            redirect('cinema_create')

    else:
        registration_form = UserRegistrationForm()
>>>>>>> 630369c3e2e9a552c8ca6173ec21b3061412630d

    context = {
        'registration_form': registration_form
    }
<<<<<<< HEAD

=======
>>>>>>> 630369c3e2e9a552c8ca6173ec21b3061412630d
    return render(request, 'user/registration.html', context=context)


def login_in(request):
    if request.method == 'POST':
        login_form_class = UserLoginForm(request.POST)
<<<<<<< HEAD

=======
>>>>>>> 630369c3e2e9a552c8ca6173ec21b3061412630d
        print(login_form_class.errors)

        if login_form_class.is_valid():
            email = login_form_class.cleaned_data['email']
<<<<<<< HEAD
            password = login_form_class.cleaned_data['password']
            print(password)
            user = authenticate(email=email, password=password)
            print(f"The user is {user}")

            if user is not None and user.is_active:
                login(request, user)
                return redirect('cinema')

            login_form_class.add_error('password', 'Password is wrong, check the writing!')

        context = {
            'login_form': login_form_class
        }

        return render(request, 'user/login.html', context=context)

    if request.user.is_anonymous:
=======
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
>>>>>>> 630369c3e2e9a552c8ca6173ec21b3061412630d
        login_form = UserLoginForm()

        context = {
            'login_form': login_form
        }
        return render(request, 'user/login.html', context=context)

    return redirect('cinema')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
