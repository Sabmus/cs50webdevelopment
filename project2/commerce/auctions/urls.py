from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("item_listed/<slug:slug>", views.item_listed, name="item_listed"),
    path("bid_item/<slug:slug>", views.bid_item, name="bid_item"),
    path("close_bid/<slug:slug>", views.close_bid, name="close_bid"),
    path("add_to_watchlist/<slug:slug>", views.add_to_watchlist, name="add_to_watchlist"),
    path("remove_from_watchlist/<slug:slug>", views.remove_from_watchlist, name="remove_from_watchlist")
]
