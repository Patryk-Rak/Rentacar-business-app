from .models import Cars, CarsReservationHistory
from rest_framework import serializers


class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'daily_rental_cost']
        # json = JSONRenderer().render(data=model)


class CarsReservationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsReservationHistory
        fields = ['day1', 'day2', 'convert_date']
        # json = JSONRenderer().render(data=model)



