# Generated by Django 4.1.3 on 2022-11-11 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_currency_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(related_name='watched_by', to='auctions.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
