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
    rotateDeg1 = serializers.IntegerField()
    rotateDeg2 = serializers.IntegerField()
    rotateDeg3 = serializers.IntegerField()
    rotateDeg4 = serializers.IntegerField()
    sizes = TileSizeSerializer(many=True)
    hasInstallationPhotos = serializers.BooleanField(required=False)
    hasSample = serializers.BooleanField()
    isSample = serializers.BooleanField()
    sampleId = serializers.IntegerField()
    new = serializers.BooleanField()
    inStock = serializers.BooleanField()
    onSale = serializers.BooleanField()


class TileDetailSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    rotateDeg1 = serializers.IntegerField()
    rotateDeg2 = serializers.IntegerField()
    rotateDeg3 = serializers.IntegerField()
    rotateDeg4 = serializers.IntegerField()
    new = serializers.BooleanField()
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
    url = serializers.CharField()


class WarehouseSerializer(BaseCatalogSerializer):
    zipcode = serializers.CharField()


class BoxSerializer(serializers.Serializer):
    description = serializers.CharField()
    measurementUnit = serializers.IntegerField()
    quantity = serializers.IntegerField()
    weight = serializers.IntegerField()


class TileOrderSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    rotateDeg1 = serializers.IntegerField()
    rotateDeg2 = serializers.IntegerField()
    rotateDeg3 = serializers.IntegerField()
    rotateDeg4 = serializers.IntegerField()
    plane = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    thickness = serializers.CharField()
    weight = serializers.CharField()
    colors = TileColorSerializer(many=True)
    uses = TileUseSerializer(many=True)
    similarTiles = SimilarTilesSerializer(many=True)
    designer = TileDesignerSerializer()
    quantity = serializers.IntegerField()
    sqFt = serializers.FloatField()
    sqFtPrice = serializers.FloatField()
    qtyIsSqFt = serializers.BooleanField()
    maximumSqFt = serializers.IntegerField()
    minimumSqFt = serializers.IntegerField()
    sample = serializers.BooleanField()
    hasSample = serializers.BooleanField()
    sampleId = serializers.IntegerField()
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
    name = serializers.CharField()
    image = serializers.CharField()
    rotateDeg1 = serializers.IntegerField()
    rotateDeg2 = serializers.IntegerField()
    rotateDeg3 = serializers.IntegerField()
    rotateDeg4 = serializers.IntegerField()
    collection = serializers.CharField()
    size = serializers.CharField()
    hasInstallationPhotos = serializers.BooleanField()
    hasSample = serializers.BooleanField()
    sampleId = serializers.IntegerField()


class GroupSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()


class GroupDesignSerializer(serializers.Serializer):
    designs = TileDesignSerializer(many=True)


class GroupTileSizeSerializer(serializers.Serializer):
    size = serializers.CharField()


class PalleteColorSerializer(serializers.Serializer):
    name = serializers.CharField()
    hexadecimalCode = serializers.CharField()


class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()


class GroupColorSerializer(serializers.Serializer):
    group = serializers.CharField()
    color = PalleteColorSerializer()    


class BasePortfolioTilesSerializer(BaseSerializer):
    name = serializers.CharField()
    image = serializers.CharField()
    sizes = TileSizeSerializer(many=True)
    url = serializers.CharField()
    colorGroups = GroupColorSerializer(required=False, many=True)
    plane = serializers.CharField(required=False)
    isCustomTile = serializers.BooleanField()


class PortfolioTilesSerializer(BasePortfolioTilesSerializer):
    portfoliotile_id = serializers.CharField()
    

class PortfolioCustomizedTilesSerializer(BasePortfolioTilesSerializer):
    customizedTileId = serializers.CharField()
    groupColors = GroupColorSerializer(many=True)


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