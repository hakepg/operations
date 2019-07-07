from rest_framework.serializers import ModelSerializer #, HyperlinkedModelSerializer
from .models import *


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class WaiterSerializer(ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
