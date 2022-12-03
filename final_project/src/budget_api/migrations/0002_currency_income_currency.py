# Generated by Django 4.1.3 on 2022-12-03 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('currency_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='budget_api.currency', verbose_name='Income currency'),
        ),
    ]
