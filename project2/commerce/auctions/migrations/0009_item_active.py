# Generated by Django 4.1.3 on 2022-11-09 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
