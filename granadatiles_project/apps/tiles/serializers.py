from rest_framework import serializers
from core.serializers import BaseGalleryImageSerializer, BaseContentSerializer, BaseCatalogSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()

class TileSerializer(BaseCatalogSerializer):
    pass


class TileDesignSerializer(BaseCatalogSerializer):
    pass


class GroupSerializer(BaseGalleryImageSerializer):
    pass


class GroupDesignSerializer(BaseContentSerializer):
    designs = TileDesignSerializer(many=True)


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()
