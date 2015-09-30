from rest_framework import serializers
from core.serializers import BaseGalleryImageSerializer, BaseContentSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()
    

class TileSerializer(BaseContentSerializer):
    pass


class GroupSerializer(BaseGalleryImageSerializer):
    pass


class GroupTileSerializer(BaseContentSerializer):
   tiles = TileSerializer(many=True)


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()