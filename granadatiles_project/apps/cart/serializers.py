from rest_framework import serializers
from core.serializers import BaseSerializer, BaseCatalogSerializer


class TileColorSerializer(BaseCatalogSerializer):
    pass


class TileSerializer(BaseCatalogSerializer):
    list_id = serializers.CharField()
    size = serializers.CharField()
    image = serializers.CharField()
    colors = TileColorSerializer(many=True)


class TileOrdersSerializer(BaseSerializer):
    sq_ft = serializers.IntegerField()
    quantity = serializers.IntegerField()
    boxes = serializers.IntegerField()
    tile = TileSerializer()


class SampleOrdersSerializer(BaseSerializer):
    quantity = serializers.IntegerField()
    tile = TileSerializer()
