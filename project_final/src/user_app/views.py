from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def login(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'post request is required.'}, status=400)

    username = request.POST["user"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password = password)

    if user is not None:
        login(request, user)
    else:
        return JsonResponse({'message': 'Either username or password are incorrect.'}, status=400)
