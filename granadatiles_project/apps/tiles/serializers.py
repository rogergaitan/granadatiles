from rest_framework import serializers
from core.serializers import BaseSerializer, BaseGalleryImageSerializer, BaseContentSerializer, BaseCatalogSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()
    menu_image = serializers.CharField()


class CollectionRetrieveSerializer(CollectionSerializer):
    introduction = serializers.CharField()


class CollectionsFilterSerializer(BaseContentSerializer):
    pass


class TileSizeSerializer(serializers.Serializer):
    size = serializers.CharField()


class TileSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    sizes = serializers.CharField()


class MainTileSerialzer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    has_installation_photos = serializers.BooleanField()


class TileDetailSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = TileSizeSerializer(many=True)


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
    image = serializers.CharField()


class WarehouseSerializer(BaseCatalogSerializer):
    zipcode = serializers.CharField()


class TileOrderSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    thickness = serializers.CharField()
    weight = serializers.CharField()
    colors = TileColorSerializer(many=True)
    uses = TileUseSerializer(many=True)
    similar_tiles = BaseCatalogSerializer(many=True)
    designer = TileDesignerSerializer()
    quantity = serializers.IntegerField()
    sample = serializers.BooleanField()
    has_sample = serializers.BooleanField()
    price = serializers.FloatField()
    tearsheet = serializers.CharField()
    ship_from = WarehouseSerializer(many=True)


class InStockSerializer(BaseCatalogSerializer):
    mosaic = serializers.CharField()
    name = serializers.CharField()
    collection = serializers.CharField()
    size = serializers.CharField()
    has_installation_photos = serializers.BooleanField()


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


class PortfolioTilesSerializer(BaseSerializer):
    name = serializers.CharField()
    sizes = TileSizeSerializer(many=True)


class LayoutSerializer(BaseSerializer):
    name = serializers.CharField()
    length_ft = serializers.CharField()
    length_in = serializers.CharField()
    width_ft = serializers.CharField()
    width_in = serializers.CharField()
    date = serializers.CharField()


class LayoutTilesSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    collection = serializers.CharField()
    size = serializers.CharField()
