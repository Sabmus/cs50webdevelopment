from django.shortcuts import render


def index(request):
    return render(request, template_name='pages/index.html', context={})


def login(request):
    return render(request, template_name='pages/user_app/login.html', context={})

def budget(request):
    return render(request, template_name='pages/budget/budget.html', context={})

