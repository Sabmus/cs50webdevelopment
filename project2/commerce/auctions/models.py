from django.contrib.auth.models import AbstractUser
from django.db import models


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
        return f"Currency: {self.name} equals to: {self.conversion_rate} {self.base_currency.name}"


class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    starting_bid = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    bid_duration = models.IntegerField()  # should be duration in days
    image = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Action #{self.id}: Item: {self.title}, staring bid: {self.starting_bid} {self.currency.name}"


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_bidded = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Bidding on: {self.auction_bidded.title} with: {self.bid_amount} {self.currency.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_commented = models.ForeignKey(Auction, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"Comment on: {self.auction_commented.title}"