from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User, auth

def homepage(request):
    context = {
        'username':request.user
    }
    return render(request, 'homepage.html', context)

def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form':login_form
    }
    
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            context['error'] = '{} login successful'.format(username)
        else:
            context['error'] = 'no such user'

    return render(request, 'auth/login.html', context)


def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        'form':register_form,
    }
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        password2 = register_form.cleaned_data.get('password2')
        user = auth.authenticate(request, username = username, password = password)
        if password2 == password:
            # register user
            user = auth.authenticate(request, username = username, password = password2)
            if user is None:
                User.objects.create_user(username, email, password2)
                context['error'] = '{} successfully registered'.format(username)
            else:
                context['error'] = 'user {} already exists. Please login'.format(username)
        else:
            context['error'] = 'Passwords do not match!'
    return render(request, 'auth/register.html', context)