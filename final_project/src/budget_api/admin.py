from django.contrib import admin

from .models import (Currency, Income, IncomeChoice, Saving, Expense, ExpenseChoice
    , TimeChoice, Investment, InvestmentChoice)



@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    fields = ('person', 'choices', 'amount', 'currency')
    list_display = ('person', 'choices', 'currency', 'created_at')


admin.site.register([Currency, IncomeChoice, Saving, Expense, ExpenseChoice
    , TimeChoice, Investment, InvestmentChoice])

