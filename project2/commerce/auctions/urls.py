from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("item_listed/<slug:slug>", views.item_listed, name="item_listed"),
    path("bid_item/<slug:slug>", views.bid_item, name="bid_item")
]
