import django_filters

from .models import Cars


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Cars
        fields = ['model', 'mark', 'year_of_production', ]