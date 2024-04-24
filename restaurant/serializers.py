from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields= ['id', 'item', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields= ['id', 'name', 'persons', 'booking_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['url', 'username', 'email', 'groups']