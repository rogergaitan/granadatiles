from rest_framework import serializers
from core.serializers import BaseGalleryImageSerializer, BaseContentSerializer, BaseCatalogSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()
    menu_image = serializers.CharField()


class CollectionRetrieveSerializer(CollectionSerializer):
    introduction = serializers.CharField()


class TileSizeSerializer(serializers.Serializer):
    name = serializers.CharField()


class TileSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    sizes = TileSizeSerializer(many=True)


class TileDesignSerializer(BaseCatalogSerializer):
    main = TileSerializer()
    tiles = TileSerializer(many=True)


class GroupSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()


class GroupDesignSerializer(serializers.Serializer):
    designs = TileDesignSerializer(many=True)


class GroupTileStyleSerializer(serializers.Serializer):
    name = serializers.CharField()


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()
