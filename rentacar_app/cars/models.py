from django.db import models
from django.shortcuts import reverse
import datetime
from facilities.models import Facility
from user_account.models import Account
import datetime



import sys
for x in sys.path:
    print(x)

# Create your models here.


class Cars(models.Model):
    CATEGORIES = (
        ('P', 'Paliwo'),
        ('D', 'Diesel'),
        ('G', 'Gaz'),
        ('E', 'Elektryk'),
        ('H', 'Hybryda'),
    )
    id = models.AutoField(primary_key=True, null=False, blank=False)
    mark = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=100, null=False, blank=False)
    year_of_production = models.PositiveSmallIntegerField(null=False, blank=False)
    color = models.CharField(max_length=100, null=False, blank=False)
    type_of_car_engine = models.CharField(max_length=20, choices=CATEGORIES)
    car_engine_power = models.PositiveSmallIntegerField(null=False, blank=False)
    mileage = models.PositiveIntegerField(null=False, blank=False)
    daily_rental_cost = models.PositiveSmallIntegerField(null=False, blank=False)
    note = models.TextField(max_length=500, null=False, blank=False)
    air_conditioner = models.BooleanField(verbose_name=("air conditioner"),
                                          default=True,
                                          help_text=("Sprawdź czy auto jest wyposażone w klimatyzację."))
    num_of_passengers = models.PositiveSmallIntegerField(null=False, blank=False)
    facility_allocation = models.ForeignKey(Facility,
                                            on_delete=models.SET_NULL,
                                            blank=True,
                                            null=True,)
    car_is_rented = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __int__(self, sale):
        self.daily_rental_cost = sale

    def __str__(self):
        return self.mark

    def saturday_sales(self):
        day_sales = datetime.datetime.today().weekday()
        if day_sales > 5:
            return "nie ma przeceny"
        else:  # 5 Sat, 6 Sun
            if self.model == "126p":
                prenctage = self.daily_rental_cost - 120
                sales_discount = prenctage
                return "jest przecena", sales_discount
            else:
                return "Brak przeceny"

    def get_url(self):
        return reverse('cars_detail',
                        args = (self.id))


class Order(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)


    # def car_rental_price(self):
    #     from datetime import datetime
    #     datetime_object_I = datetime.strptime(self.start_date, '%d/%m/%y %')
    #     datetime_object_II = datetime.strptime(self.end_date, '%d/%m/%y %')
    #     days = datetime_object_II - datetime_object_I


