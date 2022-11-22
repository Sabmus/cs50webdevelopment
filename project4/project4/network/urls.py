
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # path("following", views.following, name="following"),
    path("posts/<str:option>", views.posts, name="posts"),
    path("create_post", views.create_post, name="create_post"),
    
    # api routes
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("profile", views.profile, name="profile"),
    path("liked_post/<int:post_id>", views.liked_post, name="liked_post")
]
