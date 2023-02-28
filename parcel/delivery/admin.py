from django.contrib import admin
from .models import Parcel, DeliveryDriver, Customer
# Register your models here.

admin.site.register(Parcel)
admin.site.register(DeliveryDriver)
admin.site.register(Customer)
