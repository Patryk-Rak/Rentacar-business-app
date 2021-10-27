from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email
