# Generated by Django 4.1.3 on 2022-11-07 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('destinaton', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
