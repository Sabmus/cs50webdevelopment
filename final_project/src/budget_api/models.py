from django.db import models
from django.db.models import Sum
from base_app.models import User
from django.utils.translation import gettext as _


class Money(models.Model):
    class Meta:
        abstract = True
    
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IncomeChoice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Income(Money):
    choices = models.ForeignKey(IncomeChoice, verbose_name=_("Income choices"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.choices.name} of {super().person.username}"


class Saving(Money):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ExpenseChoice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TimeChoice(models.Model):
    name = models.CharField(max_length=10)
    short_name = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Expense(Money):
    choices = models.ForeignKey(ExpenseChoice, verbose_name=_("Expense Choice"), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_subscription = models.BooleanField(default=False)  # means that the amount is charged every month without end
    time_choice = models.ForeignKey(TimeChoice, on_delete=models.CASCADE, null=True, blank=True)
    start = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class InvestmentChoice(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Investment(Money):
    choices = models.ForeignKey(InvestmentChoice, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    return_rate = models.FloatField()
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    amount_returned = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
