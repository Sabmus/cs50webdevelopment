from django.urls import path

from . import views
from user_app.views import login as api_login

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('budget/', views.budget, name='budget'),

    # user_app
    path('login', api_login, name='login'),
]
