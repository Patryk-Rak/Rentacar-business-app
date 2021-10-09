# Generated by Django 3.2.3 on 2021-09-06 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_started', models.DateTimeField(verbose_name=datetime.date)),
                ('day_ended', models.DateTimeField(verbose_name=datetime.date)),
            ],
        ),
    ]