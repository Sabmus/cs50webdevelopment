# https://cs50.harvard.edu/web/2020/projects/2/commerce/#specification
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from . import models
from . import forms


def index(request):
    # list all available by last_until items to auction
    items = models.Item.objects.filter(last_until__gte=timezone.now()).all()
    return render(request, template_name="auctions/index.html", context={
        "items": items
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required(login_url='login')
def create_listing(request):
    if request.method == "POST":
        form = forms.CreateListingForm(request.POST)
        if form.is_valid():
            item = models.Item(**form.cleaned_data)
            item.owner = request.user
            item.save()
            # after save. update field "last_until" so be the addition of bid_duration to created_at
            record = models.Item.objects.get(pk=item.id)
            record.last_until = record.created_at + timedelta(days=record.bid_duration)
            record.save(update_fields=["last_until"])
            return HttpResponseRedirect(reverse('index'))
    else:
        form = forms.CreateListingForm()

    return render(request, "auctions/create_listing.html", context={
        "form": form
    })
