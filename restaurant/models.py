from django.db import models
from django.core.exceptions import ValidationError
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
    inventory = models.SmallIntegerField()
    
    def clean(self):
        if self.inventory < 0:
            raise ValidationError('Inventory cannot be less than 0') 
    
    def get_item(self):
        return f'{self.item} : {str(self.price)}'

class Booking(BaseModel):
    name = models.CharField(max_length=255)
    persons = models.SmallIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    