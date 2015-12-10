from rest_framework import serializers
from core.serializers import BaseSerializer, BaseCatalogSerializer


class TileColorSerializer(BaseCatalogSerializer):
    pass


class TileCartSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    colors = TileColorSerializer(many=True)


class CartSerializer(BaseSerializer):
    square_ft = serializers.IntegerField()
    quantity = serializers.IntegerField()
    boxes = serializers.IntegerField()
    tiles = TileCartSerializer(many=True)
