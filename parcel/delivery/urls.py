from django.urls import path
from .views import ParcelList, ParcelDetail, DeliveryDriverList, DeliveryDriverDetail, CustomerList, CustomerDetail

urlpatterns = [
    path('parcels/', ParcelList.as_view(), name='parcel-list'),
    path('parcels/<int:pk>/', ParcelDetail.as_view(), name='parcel-detail'),
    path('delivery-drivers/', DeliveryDriverList.as_view(), name='delivery-driver-list'),
    path('delivery-drivers/<int:pk>/', DeliveryDriverDetail.as_view(), name='delivery-driver-detail'),
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
]
