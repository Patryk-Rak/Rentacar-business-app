from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facilities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year_of_production', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('type_of_car_engine', models.CharField(choices=[('P', 'Paliwo'), ('D', 'Diesel'), ('G', 'Gaz'), ('E', 'Elektryk'), ('H', 'Hybryda')], max_length=20)),
                ('car_engine_power', models.PositiveSmallIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('daily_rental_cost', models.PositiveSmallIntegerField()),
                ('note', models.TextField(max_length=500)),
                ('air_conditioner', models.BooleanField(default=True, help_text='Sprawdź czy auto jest wyposażone w klimatyzację.', verbose_name='air conditioner')),
                ('num_of_passengers', models.PositiveSmallIntegerField()),
                ('car_is_rented', models.BooleanField(default=False)),
                ('facility_allocation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='facilities.facility')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
