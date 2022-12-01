from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from . import forms
from . import models


def register(request):
    if request.method != 'POST':
        form = forms.CreateUserForm()
        return render(request, template_name='user_app/register.html', context={
            'form': form
        })

    form = forms.CreateUserForm(request.POST)
    password = request.POST["password"]
    password_check = request.POST["password_check"]

    if password != password_check:
        return render(request, template_name='user_app/register.html', context={
            'form': form,
            'message': 'Password must match.'
        })
    else:
        try:
            validate_password(password)
        except ValidationError as ve:
            return render(request, template_name='user_app/register.html', context={
                'form': form,
                'message': ve
            })

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        email = form.cleaned_data["email"]

        try:
            user = models.User.objects.create_user(username=username, password=password, email=email)
            user.save()
        except IntegrityError:
            return render(request, template_name='user_app/register.html', context={
                'form': form,
                'message': 'An error has ocurred'
            })

        login(request, user)
        return HttpResponseRedirect(reverse('pages:budget'))
    else:
        return render(request, template_name='user_app/register.html', context={
            'form': form,
            'message': form.errors
        })



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('pages:budget'))
            else:
                return render(request, template_name='user_app/login.html', context={
                    'form': form
                })
        else:
            return render(request, template_name='user_app/login.html', context={
                    'form': form
                })
    else:
        form = AuthenticationForm()
        return render(request, template_name='user_app/login.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_app:login_view'))
