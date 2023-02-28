from rest_framework import generics
from .models import Parcel, DeliveryDriver, Customer
from .serializers import ParcelSerializer, DeliveryDriverSerializer, CustomerSerializer

class ParcelList(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class ParcelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

class DeliveryDriverList(generics.ListCreateAPIView):
    queryset = DeliveryDriver.objects.all()
    serializer_class = DeliveryDriverSerializer

class DeliveryDriverDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryDriver.objects.all()
    serializer_class = DeliveryDriverSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
