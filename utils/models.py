from django.db import models


# Create your models here.
class Address(models.Model):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    zipCode = models.PositiveIntegerField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

