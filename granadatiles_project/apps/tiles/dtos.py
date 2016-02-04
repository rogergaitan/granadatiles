from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto, BaseDto
from .models import Warehouse


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        self.menu_image = collection.menu_image.url if collection.menu_image else ''
        if language:
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()

class CollectionDetailDto(CollectionDto):

    def __init__(self, collection, language):
        super().__init__(collection, language)
        if language:
           self.introduction = collection.get_introduction(language)
        else:
           self.introduction = collection.introduction


class TileSizeDto:

    def __init__(self, size):
        self.size = size


class TileDetailDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.mosaic = tile.mosaic.url if tile.mosaic else ''
        self.image = tile.image.url if tile.image else ''
        self.uses = [TileUseDto(use, language) for use in tile.design.group.collection.uses.all()]
        self.styles = [TileStyleDto(style, language) for style in tile.design.styles.all()]
        self.colors = [TileColorDto(color, language) for color in tile.colors.all()]


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language=None):
        super().__init__(tile, language)
        self.sizes = tile.size


class MainTileDto(TileDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.mosaic = tile.mosaic.url if tile.mosaic else ''
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.hasInstallationPhotos = tile.has_installation_photos()
        self.hasSample = tile.has_sample()
        self.new = tile.new


class MinorTileDto(TileDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.mosaic = tile.mosaic.url if tile.mosaic else ''


class TileDesignDto(BaseCatalogDto):

    def __init__(self, tile_design, size, new, in_stock, specials, language=None):

        tiles_filter = tile_design.tiles.exclude(image='')
        if size: tiles_filter = tiles_filter.filter(size=size)
        if new: tiles_filter = tiles_filter.filter(new=True)
        if in_stock: tiles_filter = tiles_filter.filter(custom=False)
        if specials: tiles_filter = tiles_filter.filter(on_sale=True)

        super().__init__(tile_design, language)
        if tiles_filter:
            if tiles_filter.filter(main=True).exists():
                self.main = MainTileDto(tiles_filter.filter(main=True).first(), language)
                self.tiles = [MinorTileDto(tile, language) for tile in tiles_filter.filter(main=False)]
            else:
                #set first tile in design as main if no main tile exists
                self.main = MainTileDto(tiles_filter.first(), language)
                self.tiles = [MinorTileDto(tile, language)
                              for tile in tiles_filter.exclude(pk=self.main.id)]


class TileStyleDto(BaseCatalogDto):
    pass


class TileInstallationPhotosDto(BaseContentDto):

    def __init__(self, photo, language):
        super().__init__(photo, language)
        self.image = photo.image.url if photo.image else ''


class CollectionInstallationPhotosDto(TileInstallationPhotosDto):

    def __init__(self, photo, language):
        super().__init__(photo, language)
        self.designer = photo.designer


class SimilarTileDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.mosaic.url if tile.mosaic else ''


class TileDesignerDto(BaseContentDto):

    def __init__(self, designer, language):
        super().__init__(designer, language)


class TileColorDto(BaseCatalogDto):

    def __init__(self, color, language):
        super().__init__(color, language)
        self.hexadecimalCode = color.hexadecimalCode


class TileUseDto(BaseCatalogDto):

    def __init__(self, use, language):
        super().__init__(use, language)


class WarehouseDto(BaseCatalogDto):

    def __init__(self, warehouse, language):
        super().__init__(warehouse, language)
        self.zipcode = warehouse.zipcode


class TileOrderDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.list_id = tile.list_id
        self.image = tile.image
        self.mosaic = tile.mosaic
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.thickness = tile.thickness
        self.weight = tile.weight
        self.colors = [TileColorDto(color, language) for color in tile.colors.all()]
        self.uses = [TileUseDto(use, language) for use in tile.design.group.collection.uses.all()]
        self.styles = [TileStyleDto(style, language) for style in tile.design.styles.all()]
        self.similar_tiles = [SimilarTileDto(tile, language) for tile in tile.similar_tiles.all()]
        self.designer = TileDesignerDto(tile.design.group, language)
        self.quantity = tile.quantity_on_hand
        self.sample = tile.is_sample
        self.has_sample = tile.has_sample()
        self.price = tile.sales_price
        self.tearsheet = tile.tearsheet.url if tile.tearsheet else ''
        if tile.custom:
            self.ship_from = [WarehouseDto(warehouse, language) for warehouse in
                              Warehouse.objects.filter(custom=True)]
        else:
            self.ship_from = [WarehouseDto(warehouse, language) for warehouse in
                              Warehouse.objects.filter(custom=False)]

class InStockDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.mosaic = tile.mosaic.url if tile.mosaic else ''
        self.collection = tile.design.group.collection.get_title(language)
        self.size = tile.size
        self.has_installation_photos = tile.has_installation_photos()


class CollectionsFiltersDto(BaseContentDto):

    def __init__(self, collection, language):
        super().__init__(collection, language)


class GroupDto(BaseGalleryImageDto):
    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        if language:
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()


class MenuCollectionDto(object):
    def __init__(self, collection, language = None):
        if language:
            self.title = collection.get_title(language)
            self.url = collection.get_absolute_url(language)
        else:
            self.title = collection.title
            self.url = collection.get_absolute_url()
        self.image = collection.menu_image.url if collection.image else ''


class BasePortfolioTilesDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.list_id = tile.list_id
        self.image = tile.mosaic.url if tile.mosaic else ''
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]


class PortfolioTilesDto(BasePortfolioTilesDto):

    def __init__(self, portfoliotile_id, tile, language):
        super().__init__(tile, language)
        self.portfoliotile_id = portfoliotile_id


class PortfolioCustomTilesDto(BasePortfolioTilesDto):

    def __init__(self, customizedtile_id, tile, language):
        super().__init__(tile, language)
        self.customizedtile_id = customizedtile_id


class LayoutDto(BaseDto):

    def __init__(self, layout):
        super().__init__(layout)
        self.name = layout.name
        self.length_ft = layout.length_ft
        self.length_in = layout.length_in
        self.width_ft = layout.width_ft
        self.width_in = layout.width_in
        self.image = layout.image
        self.date = layout.date


class LayoutTilesDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.collection = tile.design.group.collection.get_title(language)
        self.image = tile.mosaic.url if tile.mosaic else ''
        self.size = tile.size
