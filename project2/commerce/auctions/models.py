from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_save
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

    def current_max_bid(self):
        max_bid = self.starting_bid
        if self.bid_maded is not None:
            max_bid = self.bid_maded.aggregate(models.Max("amount"))["amount__max"]
        return max_bid


@receiver(pre_save, sender=Item)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = util.unique_slug_generator(instance)


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bid_maded")
    amount = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Bidding on: {self.item.title} with: {self.amount} {self.currency.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment on: {self.item.title}"
