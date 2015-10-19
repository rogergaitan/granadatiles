from rest_framework import serializers
from core.serializers import BaseCatalogSerializer

class ItemSerializer(BaseCatalogSerializer):
    full_name = serializers.CharField()
    list_id = serializers.CharField()
    is_active = serializers.CharField()
    sublevel = serializers.CharField()
    sales_price = serializers.CharField()
    quantity_on_hand = serializers.CharField()
    average_cost = serializers.CharField()
    quantity_on_order = serializers.CharField()
    quantity_on_sales_order = serializers.CharField()
    sales_desc = serializers.CharField()
    purchase_desc = serializers.CharField()
    purchase_cost = serializers.CharField()
