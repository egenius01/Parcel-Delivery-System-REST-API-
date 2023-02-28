"""
Here we test the logic of the views, the model queries and the api endpoints
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Parcel, DeliveryDriver, Customer
from .serializers import ParcelSerializer, DeliveryDriverSerializer, CustomerSerializer


class ParcelTests(APITestCase):
    """
    Creating a Test case for the parcel
    """
    def setUp(self):
        """
        Createing Test customer and driver
        """
        self.delivery_driver = DeliveryDriver.objects.create(
            name='Nuel',
            email='omoragbonemmanuel@gmail.com',
            phone_number='09032530970'
        )
        self.cutomer = Customer.objects.create(
            name = 'Tolulope',
            email = 'omoragbonemmanuel@gmail.com',
            phone_number = '09032530970',
        )

    def test_create_parcel(self):
        """
        Ensure we can create a new parcel object.
        """
        url = reverse('parcel-list')
        data = {
            'tracking_id': '1234',
            'delivery_driver': 1,
            'customer': 1,
            'status': 'in transit',
            'weight': 2.5,
            'pickup_address': 'Ogba,Ikeja',
            'delivery_address': 'Ogba, Ikeja',
        }
        response = self.client.post(url, data, format='json')
        print( 'status massage =======', response)
        #This is to make sure the response returns a 201 CREATED code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Parcel.objects.count(), 1)
        self.assertEqual(Parcel.objects.get().tracking_id, '1234')

    def test_list_parcels(self):
        """
        Ensure we can list all parcel objects.
        """
        url = reverse('parcel-list')
        response = self.client.get(url, format='json')
        #This is to make sure the response returns a 200 OK code.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_parcel(self):
        """
        Ensure we can retrieve a single parcel object.
        """
        parcel = Parcel.objects.create(
            tracking_id='1234',
            delivery_driver=None,
            customer_id=1,
            status='in transit',
            weight=2.5,
            pickup_address='Ogba, Ikeja',
            delivery_address='Ogba, Ikeja',
        )
        url = reverse('parcel-detail', args=[parcel.id])
        response = self.client.get(url, format='json')
        #This is to make sure the response returns a 200 OK code.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['tracking_id'], '1234')


class DeliveryDriverTests(APITestCase):
    """
    Creating a Test case for the driver
    """
    def test_create_delivery_driver(self):
        """
        Ensure we can create a new delivery driver object.
        """
        url = reverse('delivery-driver-list')
        data = {
            'name': 'John Doe',
            'email': 'DoeNuel@gmail.com',
            'phone_number': '+234999',
        }
        response = self.client.post(url, data, format='json')
        #This is to make sure the response returns a 201 CREATED code.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DeliveryDriver.objects.count(), 1)
        self.assertEqual(DeliveryDriver.objects.get().name, 'John Doe')

    def test_list_delivery_drivers(self):
        """
        Ensure we can list all delivery driver objects.
        """
        url = reverse('delivery-driver-list')
        response = self.client.get(url, format='json')
        #This is to make sure the response returns a 200 OK code.

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_delivery_driver(self):
        """
        Ensure we can retrieve a single delivery driver object.
        """
        delivery_driver = DeliveryDriver.objects.create(
            name='John Doe',
            email='john@example.com',
            phone_number='+234999',
        )
        url = reverse('delivery-driver-detail', args=[delivery_driver.id])
        response = self.client.get(url, format='json')
        #This is to make sure the response returns a 200 OK code.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

class CustomerTests(APITestCase):
    """
    Creating a Test case for the Customer
    """
    def test_create_customer(self):
        """
        Ensure we can create a new customer object.
        """
        url = reverse('customer-list')
        data = {
            'name': 'John Nuel',
            'email': 'DoeNuel@gmail.com',
            'phone_number': '+234999'
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)