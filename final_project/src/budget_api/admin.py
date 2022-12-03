from django.contrib import admin

from .models import (Income, IncomeChoice, Saving, Expense, ExpenseChoice
    , TimeChoice, Investment, InvestmentChoice)



@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    fields = ('person', 'choices', 'amount', 'created_at', 'updated_at')
    list_display = ('person', 'choices', 'created_at')


admin.site.register([IncomeChoice, Saving, Expense, ExpenseChoice
    , TimeChoice, Investment, InvestmentChoice])

