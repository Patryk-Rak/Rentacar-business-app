from django.db import models
import datetime
# Create your models here.
from datetime import timedelta

class Event(models.Model):


    id = models.AutoField(primary_key=True, null=False, blank=False)
    # event_created = models.DateTimeField(auto_now_add=True)
    event_created = models.DateTimeField(auto_now_add=True)
    day_started = models.DateTimeField()
    day_ended = models.DateTimeField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    # def eventtime(self, day_started, day_ended):
    #     event_value = day_started + timedelta(day_ended)
    #     return event_value


