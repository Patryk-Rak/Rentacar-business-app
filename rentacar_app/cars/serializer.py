from .models import Cars, CarsReservationHistory
from rest_framework import serializers


class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'daily_rental_cost']


class CarsReservationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsReservationHistory
        fields = ['day1', 'day2', 'convert_date']




