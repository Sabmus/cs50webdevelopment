from django.urls import path

from . import views


app_name = 'budget_api'
urlpatterns = [
    path('add_income', views.add_income, name='add_income'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('add_saving', views.add_saving, name='add_saving'),
    path('add_investment', views.add_investment, name='add_investment'),
]
