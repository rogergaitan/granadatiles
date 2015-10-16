from django.db import models
from django.utils.translation import ugettext as


class Item(models.Model):
  list_id = models.CharField()
  name = models.CharField()
  full_name = models.CharField()
  is_active = models.BooleanField()
  sublevel = models.IntegerField()
  sales_price = models.FloatField()
  quantity_on_hand = models.IntegerField()
  average_cost = models.FloatField()
  quantity_on_order = models.IntegerField()
  quantity_on_sales_order = models.FloatField()
  sales_desc = models.CharField()
  purchase_desc = models.CharField()
  purchase_cost = models.FloatField()
