# Generated by Django 3.2.3 on 2021-10-30 15:09

import cars.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_started', models.DateTimeField()),
                ('day_ended', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year_of_production', models.PositiveSmallIntegerField(validators=[cars.models.validate_year])),
                ('color', models.CharField(max_length=100)),
                ('type_of_car_engine', models.CharField(choices=[('P', 'Paliwo'), ('D', 'Diesel'), ('G', 'Gaz'), ('E', 'Elektryk'), ('H', 'Hybryda')], max_length=20)),
                ('car_engine_power', models.PositiveSmallIntegerField(validators=[cars.models.validate_car_engine_power])),
                ('mileage', models.PositiveIntegerField()),
                ('daily_rental_cost', models.PositiveSmallIntegerField(validators=[cars.models.daily_rental_cost])),
                ('note', models.TextField(max_length=500)),
                ('air_conditioner', models.BooleanField(default=True, help_text='Sprawdź czy auto jest wyposażone w klimatyzację.', verbose_name='air conditioner')),
                ('num_of_passengers', models.PositiveSmallIntegerField(validators=[cars.models.validate_num_of_passengers])),
                ('car_is_rented', models.BooleanField(default=False)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.carevent')),
                ('facility_allocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='facilities.facility')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarsReservationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.DateTimeField()),
                ('day2', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cars')),
            ],
            options={
                'verbose_name': 'CarHistory',
                'verbose_name_plural': 'CarsHistory',
            },
        ),
    ]
