from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def get_incomes(self):
        return self.income_set.aggregate(Sum('amount'))["amount__sum"]
    
    def get_expenses(self):
        return self.expense_set.aggregate(Sum('amount'))["amount__sum"]

    def get_savings(self):
        return self.saving_set.aggregate(Sum('amount'))["amount__sum"]

    def get_investments(self):
        return self.investment_set.aggregate(Sum('amount'))["amount__sum"]
