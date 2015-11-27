from rest_framework import serializers
from core.serializers import BaseSerializer, BaseGalleryImageSerializer, BaseContentSerializer, BaseCatalogSerializer


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


class TileDesignerSerializer(BaseSerializer):
    title = serializers.CharField()


class TileColorSerializer(BaseCatalogSerializer):
    hexadecimalCode = serializers.CharField()


class TileUseSerializer(BaseCatalogSerializer):
    pass


class StyleSerializer(BaseCatalogSerializer):
    pass


class SimilarTilesSerializer(BaseCatalogSerializer):
    pass


class TileOrderSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = serializers.CharField()
    thickness = serializers.CharField()
    weight = serializers.CharField()
    colors = TileColorSerializer(many=True)
    uses = TileUseSerializer(many=True)
    similar_tiles = BaseCatalogSerializer(many=True)
    designer = TileDesignerSerializer()


class GroupSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()


class GroupDesignSerializer(serializers.Serializer):
    designs = TileDesignSerializer(many=True)


class GroupTileSizeSerializer(serializers.Serializer):
    sizes = serializers.CharField()


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()
