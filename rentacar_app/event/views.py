from django.shortcuts import render
from .models import Event
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EventForms
# from .models import Event


def calculated_event():
    event_value = Event.day_started - timedelta(Event.day_ended)
    return event_value


def add_event_views(request, event_id):
    submitted = False
    if request.method == "POST":
        form = EventForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse("cars-list"))
    else:
        form =EventForms
        if "submitted" in request.GET:
            submitted = True
    return render(request, "cars/add_car.html", {'form': form, 'submitted': submitted})
