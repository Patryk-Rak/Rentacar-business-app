from django.contrib import admin
from .models import Cars, CarsReservationHistory, CarEvent
from django.utils.translation import ngettext
# Register your models here.


class Admin_cars_event(admin.ModelAdmin):
    list_display = ('id', 'day_started', 'day_ended')
    search_fields = ('day_started', 'day_ended')
    ordering = ('id',)
    list_filter = ('day_started', 'day_ended',)

class Admin_cars_overview(admin.ModelAdmin):
    list_display = ('model', 'color', 'air_conditioner', 'year_of_production', 'daily_rental_cost', 'id')
    search_fields = ('model', 'category')
    ordering = ('daily_rental_cost',)
    list_filter = ('car_engine_power', 'type_of_car_engine',)


class Admin_cars_reservation(admin.ModelAdmin):
    list_display = ('car_id', 'day1', 'day2',  )
    search_fields = ('day1', 'day2')
    ordering = ('day1', )
    list_filter = ('day1', 'day2',)


admin.site.register(Cars, Admin_cars_overview)
admin.site.register(CarsReservationHistory, Admin_cars_reservation)
admin.site.register(CarEvent, Admin_cars_event)