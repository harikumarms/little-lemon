from django.db import models

class Menu(models.Model):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

class Booking(models.Model):
    name = models.CharField(max_length=255)
    persons = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)