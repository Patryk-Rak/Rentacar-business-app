from django.db import models


class Facility(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    # supervisor = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

    def __str__(self):
        return self.country + " " + self.city + " " + self.address


# class Employee_allocation(models.Model):
#     employee = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     facility = models.ForeignKey(Facility,
#                                  on_delete=models.SET_NULL,
#                                  blank=True,
#                                  null=True,)
