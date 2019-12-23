from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def homepage(request):
    return render(request, 'homepage.html')

def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form,
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html', context)

def login(request):
    login_form = LoginForm(request.POST or None)
    context = {
        'form':login_form
    }

    if login_form.is_valid():
        print(login_form.cleaned_data)

    return render(request, 'auth/login.html', context)

def register(request):
    context = {

    }

    return render(request, 'auth/register.html', context)