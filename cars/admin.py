from django.contrib import admin
from .models import Cars, CarsReservationHistory


class AdminCarsOverview(admin.ModelAdmin):
    list_display = ('model', 'color', 'air_conditioner', 'year_of_production', 'daily_rental_cost', 'id')
    search_fields = ('model', 'category')
    ordering = ('daily_rental_cost',)
    list_filter = ('car_engine_power', 'type_of_car_engine',)


class AdminCarsReservation(admin.ModelAdmin):
    list_display = ('car_id', 'day1', 'day2',  )
    search_fields = ('day1', 'day2')
    ordering = ('day1', )
    list_filter = ('day1', 'day2',)


admin.site.register(Cars, AdminCarsOverview)
admin.site.register(CarsReservationHistory, AdminCarsReservation)
