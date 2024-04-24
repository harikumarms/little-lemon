from datetime import timezone
from django.db import models
from jsonschema import ValidationError
from django.db.models import F, Q
from django.db.models.functions import Now

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Menu(BaseModel):
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    
    def clean(self):
        if self.inventory < 0:
            raise ValidationError('Inventory cannot be less than 0')        

class Booking(BaseModel):
    name = models.CharField(max_length=255)
    persons = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(booking_date__lte=Now()),
                name="booking_date_constraint"
            )
        ]
        