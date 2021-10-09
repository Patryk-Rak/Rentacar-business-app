from django.contrib import admin
from .models import Event


class admin_event_overview(admin.ModelAdmin):
    # list_display = ('day_started', 'day_ended')
    search_fields = ('day_started', 'day_ended')
    ordering = ('id',)
    # list_filter = ('day_started', 'day_ended',)


admin.site.register(Event, admin_event_overview)

