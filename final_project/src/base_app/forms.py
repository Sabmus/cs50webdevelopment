from django import forms
from django.forms import ModelForm

from budget_api import models


class CreateUserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25, required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label="Password", max_length=50, required=True, widget=forms.widgets.PasswordInput)
    password_check = forms.CharField(label="Password Check", max_length=50, required=True, widget=forms.widgets.PasswordInput)


class AddIncomeForm(ModelForm):
    class Meta:
        model = models.Income
        fields = ['choices', 'amount','currency']
