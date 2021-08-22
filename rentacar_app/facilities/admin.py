from django.contrib import admin
from .models import Facility
# Register your models here.


class Admin_facilities_overview(admin.ModelAdmin):
    list_display = ('country', 'city', 'address')
    search_fields = ('country', 'city', 'address')
    ordering = ('country',)
    list_filter = ('country', 'city')


admin.site.register(Facility, Admin_facilities_overview)

# class Admin_employees_overview(admin.ModelAdmin):
#     list_display = ('employee', 'facility')
#     search_fields = ('employee', 'facility')
#     ordering = ('facility',)
#     list_filter = ('employee', 'facility')
#
#
# admin.site.register(Employee_allocation, Admin_employees_overview)
