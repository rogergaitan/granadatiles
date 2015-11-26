from rest_framework import serializers
from core.serializers import BaseGalleryImageSerializer, BaseContentSerializer, BaseCatalogSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()
    menu_image = serializers.CharField()


class CollectionRetrieveSerializer(CollectionSerializer):
    introduction = serializers.CharField()


class TileSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    sizes = serializers.CharField()

class MainTileSerialzer(BaseCatalogSerializer):
    image = serializers.CharField()
    sizes = serializers.ListField(
            child = serializers.CharField()
        )

class TileDetailSerializer(BaseCatalogSerializer):
    mosaic = serializers.CharField()
    sizes = serializers.CharField()


class TileInstallationPhotosSerializer(BaseContentSerializer):
    image = serializers.CharField()


class TileDesignSerializer(BaseCatalogSerializer):
    main = MainTileSerialzer()
    tiles = TileSerializer(many=True)


class TileOrderSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = serializers.CharField()
    thickness = serializers.CharField()
    weight = serializers.CharField()
    colors = serializers.CharField()
    uses = serializers.CharField()


class GroupSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()


class GroupDesignSerializer(serializers.Serializer):
    designs = TileDesignSerializer(many=True)


class GroupTileStyleSerializer(serializers.Serializer):
    name = serializers.CharField()


class GroupTileSizeSerializer(serializers.Serializer):
    sizes = serializers.CharField()


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()
