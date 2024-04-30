import json
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
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
        
        
class CustomJWTTokenseralizers(TokenObtainPairSerializer):

    @classmethod    
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['username'] = user.username
        return token