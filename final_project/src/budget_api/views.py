from django.shortcuts import render
from django.http import JsonResponse
import json

from . import models
from budget_api import forms


def add_income(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'Post request required.'}, status=403)

    body = json.loads(request.body)
    form_dict = {
        'choices': int(body['choices']),
        'amount': int(body['amount']),
        'currency': int(body['currency'])
    }

    form = forms.AddIncomeForm(form_dict)
    if form.is_valid():
        income = models.Income.objects.create(
            person = request.user,
            **form.cleaned_data
        )
        income.save()
        return JsonResponse({'message': 'form valid'}, status=200)
    else:
        return JsonResponse({'message': 'form not valid'}, status=400)
    

def add_expense(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'Post request required.'}, status=403)

    body = json.loads(request.body)
    if int(body['is_subscription']):
        form_dict = {
            'choices': int(body['choices']),
            'name': body['name'],
            'amount': int(body['amount']),
            'currency': int(body['currency']),
            'is_subscription': int(body['is_subscription']),
            'time_choice': int(body['time_choice']),
            'start': body['start']
        }
    else:
        form_dict = {
            'choices': int(body['choices']),
            'name': body['name'],
            'amount': int(body['amount']),
            'currency': int(body['currency']),
            'is_subscription': None,
            'time_choice': None,
            'start': None
        }

    form = forms.AddExpenseForm(form_dict)
    if form.is_valid():
        expense = models.Expense.objects.create(
            person = request.user,
            **form.cleaned_data
        )
        expense.save()
        return JsonResponse({'message': 'form valid'}, status=200)
    else:
        return JsonResponse({'message': 'form not valid'}, status=400)


def add_saving(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'Post request required.'}, status=403)

    body = json.loads(request.body)
    form_dict = {
        'name': body['name'],
        'amount': int(body['amount']),
        'currency': int(body['currency'])
    }

    form = forms.AddSavingForm(form_dict)
    if form.is_valid():
        saving = models.Saving.objects.create(
            person = request.user,
            **form.cleaned_data
        )
        saving.save()
        return JsonResponse({'message': 'form valid'}, status=200)
    else:
        return JsonResponse({'message': 'form not valid'}, status=400)


def add_investment(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'Post request required.'}, status=403)

    body = json.loads(request.body)
    form_dict = {
        'choices': int(body['choices']),
        'name': body['body'],
        'amount': int(body['amount']),
        'currency': int(body['currency']),
        'return_rate': float(body['return_rate']),
        'start': body['start'],
        'end': body['end'],
        'amount_returned': int(body['amount_returned'])
    }

    form = forms.AddInvestmentForm(form_dict)
    if form.is_valid():
        investment = models.Investment.objects.create(
            person = request.user,
            **form.cleaned_data
        )
        investment.save()
        return JsonResponse({'message': 'form valid'}, status=200)
    else:
        return JsonResponse({'message': 'form not valid'}, status=400)
