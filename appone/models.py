from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    expiry_date_time = models.DateTimeField()

    def is_expired(self):
        return self.expiry_date_time < timezone.now()

    def status(self):
        return "Expired" if self.is_expired() else "Active"

    def __str__(self):
        return f"{self.name} ({self.status()})"
