from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import timedelta

from . import util


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class BaseCurrency(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=7)
    base_currency = models.ForeignKey(BaseCurrency, on_delete=models.CASCADE)
    conversion_rate = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name}"


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    starting_bid = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    bid_duration = models.IntegerField()  # should be duration in days
    image = models.URLField(max_length=200, blank=True, default="https://apply.sts.net.pk/assets/images/default-upload-image.jpg")
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_until = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False, blank=True)

    def __str__(self) -> str:
        return f"Action #{self.id}: Item: {self.title}, staring bid: {self.starting_bid} {self.currency.name}"


@receiver(pre_save, sender=Item)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = util.unique_slug_generator(instance)

    if not instance.last_until:
        instance.last_until = instance.created_at + timedelta(days=instance.bid_duration)


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Bidding on: {self.item.title} with: {self.amount} {self.currency.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment on: {self.item.title}"
