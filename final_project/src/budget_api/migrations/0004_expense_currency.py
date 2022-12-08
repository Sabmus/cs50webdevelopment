# Generated by Django 4.1.3 on 2022-12-06 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget_api', '0003_alter_income_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget_api.currency', verbose_name='Expense currency'),
        ),
    ]