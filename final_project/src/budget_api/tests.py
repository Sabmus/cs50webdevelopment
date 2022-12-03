from django.test import TestCase
# from django.utils import timezone
from django.db.models import Sum

from . import models
from base_app.models import User

class IncomeTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='user1', password='password1', email='user1@users.com')
        models.IncomeChoice.objects.create(name='income1')
        models.IncomeChoice.objects.create(name='income2')
        models.ExpenseChoice.objects.create(name='expense1')
        models.TimeChoice.objects.create(name='year', short_name='Y')

    def test_user_exists(self):
        user1 = User.objects.get(username='user1')
        self.assertEqual(user1.pk, 1)

    def test_get_total_income(self):
        user1 = User.objects.get(username='user1')
        income1 = models.IncomeChoice.objects.get(name='income1')
        income2 = models.IncomeChoice.objects.get(name='income2')
        expense1 = models.ExpenseChoice.objects.get(name='expense1')

        models.Income.objects.create(
            person=user1,
            amount=100,
            choices=income1
        )
        models.Income.objects.create(
            person=user1,
            amount=100,
            choices=income2
        )

        total_income = user1.income_set.aggregate(Sum('amount'))
        self.assertEqual(total_income["amount__sum"], 200)

    def test_get_total_expenses(self):
        user1 = User.objects.get(username='user1')
        expense1 = models.ExpenseChoice.objects.get(name='expense1')

        models.Expense.objects.create(
            person=user1,
            amount=50,
            choices=expense1,
            name='expense1_name'
        )
        
        total_expense = user1.expense_set.aggregate(Sum('amount'))
        self.assertEqual(total_expense["amount__sum"], 50)

    def test_get_income_from_user(self):
        user1 = User.objects.get(username='user1')
        income1 = models.IncomeChoice.objects.get(name='income1')

        models.Income.objects.create(
            person=user1,
            amount=100,
            choices=income1
        )

        income = user1.get_incomes()
        print(income)
        
        self.assertEqual(income, 100)
