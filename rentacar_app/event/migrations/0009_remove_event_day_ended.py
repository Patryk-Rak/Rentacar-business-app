# Generated by Django 3.2.3 on 2021-10-07 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_auto_20210926_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='day_ended',
        ),
    ]