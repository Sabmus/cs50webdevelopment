# https://cs50.harvard.edu/web/2020/projects/4/network/#specification
# https://docs.djangoproject.com/en/4.1/ref/request-response/#jsonresponse-objects
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from . import models


def index(request):
    # check if logged in, else redirect to login
    if request.user.is_authenticated:
        posts = models.Post.objects.all().order_by('-created_at')
        return render(request, "network/index.html", context={
            'posts': posts
        })
    else:
        return HttpResponseRedirect(reverse('login'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = models.User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def following(request):
    if request.user.is_authenticated:
        following = models.User.objects.filter(follower__exact=request.user)
        posts = models.Post.objects.filter(author__in=following).order_by('-created_at')
        return render(request, template_name='network/following.html', context={
            'posts': posts
        })
    else:
        return HttpResponseRedirect(reverse('login'))
        

def create_post(request):
    if request.method != "POST":
        return JsonResponse({'message': 'POST request required.'}, status=400)
    else:
        return JsonResponse({'message': 'OK'}, status=200)


def edit_post(request, post_id):
    pass


def profile(request):
    return HttpResponse(request)


def liked_post(request, post_id):
    pass


