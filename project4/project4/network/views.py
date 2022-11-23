# https://cs50.harvard.edu/web/2020/projects/4/network/#specification
# https://docs.djangoproject.com/en/4.1/ref/request-response/#jsonresponse-objects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from . import models
from . import forms


@login_required(login_url='login')
def index(request):
    return render(request, template_name='network/index.html', context={})


def all_posts(request):
    return render(request, template_name='network/posts.html', context={})


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


@login_required(login_url='login')
def posts(request, option):
    if request.method == 'GET':
        if option == 'all':
            posts = models.Post.objects.all().order_by('-created_at')
            
            paginator = Paginator(posts, 2)  # show 10 post per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return JsonResponse([post.serialize() for post in page_obj], safe=False, status=200)
        if option == 'following':
            following = models.User.objects.filter(follower__exact=request.user)
            posts = models.Post.objects.filter(author__in=following).order_by('-created_at')
            return JsonResponse([post.serialize() for post in posts], safe=False, status=200)

    return JsonResponse({'message': 'required GET method.'}, status=400)


@login_required(login_url='login')
def create_post(request):
    post_form = forms.PostForm(request.POST)

    if request.method != "POST":
        return render(request, template_name='network/index.html', context={
            'post_form': post_form,
            'message': 'POST request is required.'
        })
    
    if not post_form.is_valid():
         return render(request, template_name='network/index.html', context={
            'post_form': post_form,
            'message': 'Please check you input.'
        })


    post = models.Post(**post_form.cleaned_data)
    post.author = request.user
    post.save()

    return HttpResponseRedirect(reverse('all_posts'))


@login_required(login_url='login')
def edit_post(request, post_id):
    pass


@login_required(login_url='login')
def profile(request, username):
    profile_user = models.User.objects.get(username=username)
    posts = models.Post.objects.filter(author__exact=profile_user)

    return render(request, template_name='network/profile.html', context={
        'can_follow': request.user != profile_user,  # return False is the logged user is different than the profile user
        'follower': profile_user.follower.count(),
        'following': profile_user.following(),
        'posts': posts
    })


@login_required(login_url='login')
def liked_post(request, post_id):
    try:
        post = models.Post.objects.get(pk=post_id)
    except models.Post.IntegrityError as error:
        return JsonResponse({'message': error}, status=500)

    # if user not liked the post add to liked list, else remove it
    if request.user not in post.liked_by.all():
        post.liked_by.add(request.user)
        return JsonResponse({'message': 'post liked!', 'likes': post.like_count}, status=200)
    else:
        post.liked_by.remove(request.user)
        return JsonResponse({'message': 'post not liked!', 'likes': post.like_count}, status=200)
