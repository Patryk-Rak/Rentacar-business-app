from django.contrib import admin
from .models import Facility


class AdminFacilitiesOverview(admin.ModelAdmin):
    list_display = ('country', 'city', 'address')
    search_fields = ('country', 'city', 'address')
    ordering = ('country',)
    list_filter = ('country', 'city')


admin.site.register(Facility, AdminFacilitiesOverview)
