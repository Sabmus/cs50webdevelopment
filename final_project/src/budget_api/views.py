from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    if request.user.is_authenticated:
        return JsonResponse({'message': 'hello from Api'}, status=200)
    else:
        return JsonResponse({'message': 'must be logged in'}, status=403)


