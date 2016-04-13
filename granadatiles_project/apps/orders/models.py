from django.db import models
from django.contrib.auth.models import User

from apps.tiles.models import Tile, CustomizedTile, Box


class Address(models.Model):
    ADDRESS_TYPES = (
        (1, 'Billing'),
        (2, 'Shipping')
    )
    
    order = models.ForeignKey('Order')
    street_building_house_line1 = models.CharField(max_length=80)
    house_apt_line2 = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=20)
    province_state = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    type = models.CharField(max_length=1, choices=ADDRESS_TYPES)
    
    def __str__(self):
        return ('Billing Address' if self.type == 1 else 'Shipping Address')
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    
    
class Order(models.Model):
    customer_first_name = models.CharField(max_length=30, verbose_name='Customer First Name')
    customer_last_name = models.CharField(max_length=30, verbose_name='Customer Last Name')
    customer_company_name = models.CharField(max_length=50, verbose_name='Customer Company Name')
    credit_cart_number = models.CharField(max_length=12, blank=True, null=True, verbose_name='Credit Card Number')
    ip_address = models.GenericIPAddressField(verbose_name='IP Address')
    user = models.ForeignKey(User, related_name='+', blank=True, null=True)
    same_as_shipping = models.BooleanField()
    
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order)
    tile = models.ForeignKey(Tile, null=True, blank=True)
    customized_tile = models.ForeignKey(CustomizedTile, null=True, blank=True)
    input_sq_ft = models.PositiveIntegerField()
    price_per_sq_ft = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_tile = models.DecimalField(max_digits=10, decimal_places=2)
    base_cost = models.DecimalField(max_digits=10, decimal_places=2)
    box = models.ForeignKey(Box)