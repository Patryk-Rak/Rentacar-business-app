from django import forms
from django.forms import ModelForm
from .models import Event


class EventForms(forms.ModelForm):
    class Meta:
        model = Event
        # field = ('day_started', "day_ended")
        exclude = []