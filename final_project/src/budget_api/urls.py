from django.urls import path

from . import views


app_name = 'budget_api'
urlpatterns = [
    path('add_income', views.add_income, name='add_income')
]
