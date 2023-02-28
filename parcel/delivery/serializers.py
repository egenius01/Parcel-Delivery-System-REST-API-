"""
The Serializer is what basically converts the info from django database to JSON.
"""

from rest_framework import serializers
from .models import Parcel, DeliveryDriver, Customer

class ParcelSerializer(serializers.ModelSerializer):
    "Converts the parcel data"
    class Meta:
        model = Parcel
        fields = '__all__'

class DeliveryDriverSerializer(serializers.ModelSerializer):
    """
    Converts the Drivers Data
    """
    class Meta:
        model = DeliveryDriver
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    """
    Converts the Customers data
    """
    class Meta:
        model = Customer
        fields = '__all__'
