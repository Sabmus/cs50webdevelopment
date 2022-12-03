from django.urls import path

from . import views


app_name = 'base_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('add_income', views.add_income, name='add_income')
]
