from rest_framework import serializers
from core.serializers import BaseSerializer, BaseCatalogSerializer


class TileCartSerializer(BaseCatalogSerializer):
    colors = serializers.CharField()
    image = serializers.CharField()


class CartSerializer(BaseSerializer):
    square_ft = serializers.IntegerField()
    quantity = serializers.IntegerField()
    boxes = serializers.IntegerField()
    tiles = TileCartSerializer(many=True)
