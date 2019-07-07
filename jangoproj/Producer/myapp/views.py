from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class PlaceOp(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class RestaurantOp(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class WaiterOp(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class CustomerOp(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

