from django.urls import path

from . import views


app_name = 'base_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('add_income', views.add_income, name='add_income'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('add_saving', views.add_saving, name='add_saving'),
    path('add_investment', views.add_investment, name='add_investment'),
]
