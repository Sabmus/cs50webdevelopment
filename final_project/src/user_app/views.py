from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, template_name='user_app/index.html', context={})


def register(request):
    pass


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('budget:index'))
        else:
            return render(request, template_name='user_app/login.html', context={
                'message': ''
            })
                
                

    

    


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_app:login'))
