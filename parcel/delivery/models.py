"""
The Models file where I define how the data is stored in the database.
"""
from django.db import models

class Parcel(models.Model):
    """
    Parcel to be delivered
    """
    tracking_id = models.CharField(max_length=50)
    delivery_driver = models.ForeignKey('DeliveryDriver', on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    pickup_address = models.CharField(max_length=200)
    delivery_address = models.CharField(max_length=200)

class DeliveryDriver(models.Model):
    """
    Driver of the item to be delivered
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

class Customer(models.Model):
    """
     Customer Whose Item is to be delivered
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
