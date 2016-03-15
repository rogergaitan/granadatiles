from rest_framework import serializers
from core.serializers import BaseSerializer, BaseCatalogSerializer


class TileColorSerializer(BaseCatalogSerializer):
    pass


class TileSerializer(BaseCatalogSerializer):
    size = serializers.CharField()
    image = serializers.CharField()
    colors = TileColorSerializer(many=True)
    inStock = serializers.BooleanField()


class BaseTileOrdersSerializer(BaseSerializer):
    sqFt = serializers.IntegerField()
    quantity = serializers.IntegerField()
    boxes = serializers.IntegerField()
    subtotal = serializers.FloatField()


class TileOrdersSerializer(BaseTileOrdersSerializer):
    tile = TileSerializer()


class GroupColorSerializer(serializers.Serializer):
    group = serializers.CharField()
    color_name = serializers.CharField()
    color_code = serializers.CharField()


class CustomizedTileOrdersSerializer(BaseTileOrdersSerializer):
    tile = TileSerializer()
    group_colors = GroupColorSerializer(many=True)


class BaseSampleOrdersSerializer(BaseSerializer):
    quantity = serializers.IntegerField()
    subtotal = serializers.FloatField()


class SampleOrdersSerializer(BaseSampleOrdersSerializer):
    tile = TileSerializer()


class CustomizedSampleOrdersSerializer(BaseSampleOrdersSerializer):
    tile = TileSerializer()
    group_colors = GroupColorSerializer(many=True)
