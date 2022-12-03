from django.shortcuts import render
from django.http import JsonResponse
import json

from . import models
from base_app import forms


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
            amount = int(form.cleaned_data['amount']),
            choices_id = form_dict['choices'],
            currency_id = form_dict['currency']
        )
        income.save()
        return JsonResponse({'message': 'form valid'}, status=200)
    else:
        return JsonResponse({'message': 'form not valid'}, status=400)
    

def add_expense(request):
    pass