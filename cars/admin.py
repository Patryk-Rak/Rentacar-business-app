from django.contrib import admin
from .models import Cars
from django.utils.translation import ngettext
# Register your models here.



class Admin_cars_overview(admin.ModelAdmin):
    list_display = ('model', 'color', 'air_conditioner', 'year_of_production', 'daily_rental_cost')
    search_fields = ('model', 'category')
    ordering = ('daily_rental_cost',)
    list_filter = ('car_engine_power', 'type_of_car_engine',)



admin.site.register(Cars, Admin_cars_overview)
