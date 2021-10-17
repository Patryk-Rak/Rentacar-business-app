# Generated by Django 3.2.3 on 2021-09-19 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='daily_rental_cost',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('test', models.CharField(max_length=10)),
                ('approved', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('canceled', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]