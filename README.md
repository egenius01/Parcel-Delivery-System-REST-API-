# Parcel Delivery System (REST-API)
This is a Django Rest application for a parcel delivery system covering at least 5 use cases, 3 entities and two user types.

## Entities:
1. Parcel
2. Delivery Driver
3. Customer

## User Types:
1. Admin
2. Delivery Driver

## Use Cases:
1. Admin can add/update/delete a parcel to the system
2. Delivery Driver can view the list of parcels assigned to them for delivery
3. Delivery Driver can update the status of a parcel (delivered, in transit, etc.)
4. Customer can view the status of their parcel using a tracking ID
5. Customer can update the delivery address of their parcel

# Getting Started

## Requirements

1. Python 3.6+
2. Django 4.1,

# Installation
Make sure your virtual environment is started (venv) in the project.
Install using pip in terminal... 

``` pip install django djangorestframework ```

In the Terminal start the server by typing:

> python manage.py runserver

... then type enter.

Test The Project by typing:

> python manage.py test
 



