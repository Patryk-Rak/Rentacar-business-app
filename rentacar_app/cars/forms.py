from django import forms
from django.forms import ModelForm

from .models import Cars, CarsReservationHistory
import datetime #Create a Cars form



class CarsForm(ModelForm):

    class Meta:
        model = Cars
        fields = "__all__" #można zaimportować całośc

        widgets = {
            'mark' : forms.TextInput(attrs={'class':'form-control'}),
            'model' : forms.TextInput(attrs={'class':'form-control'}),
            'color' : forms.TextInput(attrs={'class':'form-control'}),
            'note' : forms.TextInput(attrs={'class':'form-control'}),
            }


class DateInput(forms.DateInput):
    input_type = 'date'



class CarsReservationHistoryForm(forms.ModelForm):
    # day1 = forms.DateTimeField(required=True)
    # day2 = forms.DateTimeField(required=True)
    class Meta:
        model = CarsReservationHistory
        fields = ('car', 'day1', 'day2', )
        widgets = {
            'day1': DateInput(),
            'day2': DateInput(),
        }

    def convert_date(self, day1, day2):
        day1 = datetime.datetime.combine(day1.date(), day1.time())
        day2 = datetime.datetime.combine(day2.date(),day2.time())
        total_value = day2 - day1
        return total_value


