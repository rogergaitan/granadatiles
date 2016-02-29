from rest_framework import serializers
from core.serializers import BaseSerializer, BaseGalleryImageSerializer, BaseContentSerializer, BaseCatalogSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()
    menu_image = serializers.CharField()


class CollectionRetrieveSerializer(CollectionSerializer):
    introduction = serializers.CharField()


class CollectionsFilterSerializer(BaseSerializer):
    title = serializers.CharField()


class TileUseSerializer(BaseCatalogSerializer):
    pass


class TileColorSerializer(BaseCatalogSerializer):
    hexadecimalCode = serializers.CharField()


class StyleSerializer(BaseCatalogSerializer):
    pass


class TileSizeSerializer(serializers.Serializer):
    size = serializers.CharField()


class TileSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    sizes = serializers.CharField()
    onSale = serializers.BooleanField()

class MainTileSerialzer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    hasInstallationPhotos = serializers.BooleanField(required=False)
    hasSample = serializers.BooleanField()
    new = serializers.BooleanField()
    inStock = serializers.BooleanField()
    onSale = serializers.BooleanField()


class TileDetailSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    uses = TileUseSerializer(many=True)
    styles = StyleSerializer(many=True)
    colors = TileColorSerializer(many=True)


class TileInstallationPhotosSerializer(BaseContentSerializer):
    image = serializers.CharField()


class CollectionInstallationPhotosSerializer(TileInstallationPhotosSerializer):
    designer = serializers.CharField()


class TileDesignSerializer(BaseCatalogSerializer):
    main = MainTileSerialzer(required=False)
    tiles = TileSerializer(many=True, required=False)


class TileDesignerSerializer(BaseSerializer):
    title = serializers.CharField()


class SimilarTilesSerializer(BaseCatalogSerializer):
    image = serializers.CharField()


class WarehouseSerializer(BaseCatalogSerializer):
    zipcode = serializers.CharField()


class BoxSerializer(serializers.Serializer):
    description = serializers.CharField()
    measurementUnit = serializers.IntegerField()
    quantity = serializers.IntegerField()


class TileOrderSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    mosaic = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    thickness = serializers.CharField()
    weight = serializers.CharField()
    colors = TileColorSerializer(many=True)
    uses = TileUseSerializer(many=True)
    similarTiles = BaseCatalogSerializer(many=True)
    designer = TileDesignerSerializer()
    quantity = serializers.IntegerField()
    sqFt = serializers.FloatField()
    sqFtPrice = serializers.FloatField()
    qtyIsSqFt = serializers.BooleanField()
    maximumSqFt = serializers.IntegerField()
    minimumSqFt = serializers.IntegerField()
    sample = serializers.BooleanField()
    hasSample = serializers.BooleanField()
    inPortfolio = serializers.BooleanField()
    hasInstallationPhotos = serializers.BooleanField()
    inStock = serializers.BooleanField()
    price = serializers.FloatField()
    tearsheet = serializers.CharField()
    styles = StyleSerializer(many=True)
    box = BoxSerializer(required=False)
    leadTime = serializers.CharField()
    shipFrom = WarehouseSerializer(many=True)


class InStockSerializer(BaseCatalogSerializer):
    mosaic = serializers.CharField()
    name = serializers.CharField()
    collection = serializers.CharField()
    size = serializers.CharField()
    hasInstallationPhotos = serializers.BooleanField()
    hasSample = serializers.BooleanField()


class GroupSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()


class GroupDesignSerializer(serializers.Serializer):
    designs = TileDesignSerializer(many=True)


class GroupTileSizeSerializer(serializers.Serializer):
    size = serializers.CharField()


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()


class BasePortfolioTilesSerializer(BaseSerializer):
    list_id = serializers.CharField()
    name = serializers.CharField()
    image = serializers.CharField()
    sizes = TileSizeSerializer(many=True)


class PortfolioTilesSerializer(BasePortfolioTilesSerializer):
    portfoliotile_id = serializers.CharField()


class PortfolioCustomTilesSerializer(BasePortfolioTilesSerializer):
    customizedtile_id = serializers.CharField()


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
