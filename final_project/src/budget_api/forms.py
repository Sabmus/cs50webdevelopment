from django import forms
from django.forms import ModelForm

from . import models
 

class AddIncomeForm(ModelForm):
    class Meta:
        model = models.Income
        fields = ['choices', 'amount', 'currency']


class AddExpenseForm(ModelForm):
    class Meta:
        model = models.Expense
        fields = ['choices', 'name', 'amount', 'currency', 'is_subscription', 'time_choice', 'start']
        widgets = {
            'start': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class AddSavingForm(ModelForm):
    class Meta:
        model = models.Saving
        fields = ['name', 'amount', 'currency']


class AddInvestmentForm(ModelForm):
    class Meta:
        model = models.Investment
        fields = ['choices', 'name', 'amount', 'currency', 'return_rate', 'start', 'end', 'amount_returned']
        widgets = {
            'start': forms.widgets.DateInput(attrs={'type': 'date'}),
            'end': forms.widgets.DateInput(attrs={'type': 'date'})
        }
