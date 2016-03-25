from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto, BaseDto
from .models import Warehouse, LeadTime


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        self.menu_image = collection.menu_image.url if collection.menu_image else ''
        if language:
            self.menuTitle = collection.get_menu(language)
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()
            self.menuTitle = collection.menu_title

class CollectionDetailDto(CollectionDto):

    def __init__(self, collection, language):
        super().__init__(collection, language)
        if language:
           self.introduction = collection.get_introduction(language)
           self.menuTitle = collection.get_menu(language)
        else:
           self.introduction = collection.introduction
           self.menuTitle = collection.menu_title


class TileSizeDto:

    def __init__(self, size):
        self.size = size


class TileDetailDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.image = tile.image.url if tile.image else ''
        self.rotateDeg1 = tile.rotate_deg1
        self.rotateDeg2 = tile.rotate_deg2
        self.rotateDeg3 = tile.rotate_deg3
        self.rotateDeg4 = tile.rotate_deg4
        self.new = tile.new
        self.uses = [TileUseDto(use, language) for use in tile.design.group.collection.uses.all()]
        self.styles = [TileStyleDto(style, language) for style in tile.design.styles.all()]
        self.colors = [TileColorDto(color, language, colorIsDict=True) for color in tile.colors.values('color__id', 'color__name', 'color__hexadecimalCode').distinct()]


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language=None):
        super().__init__(tile, language)
        self.sizes = tile.size


class MainTileDto(BaseDto):

    def __init__(self, tile, language):
        import re

        super().__init__(tile)
        if language:
            self.name = tile.get_name(language)
        else:
	    #filter tile name if match
            m = re.search('- In Stock', tile.name, re.I)
            self.name = tile.name[:m.start() - 1] if m else tile.name
        self.sizes = tile.size
        self.image = tile.image.url if tile.image else ''
        self.rotateDeg1 = tile.rotate_deg1
        self.rotateDeg2 = tile.rotate_deg2
        self.rotateDeg3 = tile.rotate_deg3
        self.rotateDeg4 = tile.rotate_deg4
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.hasInstallationPhotos = tile.has_installation_photos()
        self.isSample = tile.is_sample
        if self.isSample:
            self.sampleId = tile.id
        else:
            self.sampleId = tile.sample.id if tile.sample else 0
        self.hasSample = tile.has_sample() if not tile.is_sample else True
        self.new = tile.new
        self.inStock = False if tile.custom == True else True
        self.onSale = True if tile.on_sale else False


class MinorTileDto(TileDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.onSale = True if tile.on_sale else False


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
        self.image = tile.image.url if tile.image else ''
        self.url = tile.get_absolute_url(language)


class TileDesignerDto(BaseContentDto):

    def __init__(self, designer, language):
        super().__init__(designer, language)


class TileColorDto(BaseCatalogDto):

    def __init__(self, color, language, colorIsDict = False):
        if colorIsDict:
            self.id = color['color__id']
            self.name = color['color__name']
            self.hexadecimalCode = color['color__hexadecimalCode']
        else:
            super().__init__(color, language)
            self.hexadecimalCode = color.hexadecimalCode
            self.id = color.id


class TileUseDto(BaseCatalogDto):

    def __init__(self, use, language):
        super().__init__(use, language)


class WarehouseDto(BaseCatalogDto):

    def __init__(self, warehouse, language):
        super().__init__(warehouse, language)
        self.zipcode = warehouse.zipcode


class BoxDto:

    def __init__(self, box):
        self.description = box.description
        self.measurementUnit = box.measurement_unit
        self.quantity = box.quantity
        self.weight = box.weight


class LeadTimeDto(BaseContentDto):

    def __init__(self, lead_time, language):
        super().__init__(lead_time, language)


class TileOrderDto(BaseCatalogDto):

    def __init__(self, tile, portfolio, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.rotateDeg1 = tile.rotate_deg1
        self.rotateDeg2 = tile.rotate_deg2
        self.rotateDeg3 = tile.rotate_deg3
        self.rotateDeg4 = tile.rotate_deg4
        self.plane = tile.plane.url if tile.plane else ''
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.thickness = tile.thickness
        self.weight = tile.weight
        self.colors = [TileColorDto(color, language, colorIsDict=True) for color in tile.colors.values('color__id', 'color__name', 'color__hexadecimalCode').distinct()]
        self.colorGroups = [GroupColorDto(colorGroup, language) for colorGroup in tile.colors.all()]
        self.uses = [TileUseDto(use, language) for use in tile.design.group.collection.uses.all()]
        self.styles = [TileStyleDto(style, language) for style in tile.design.styles.all()]
        self.similarTiles = [SimilarTileDto(tile, language) for tile in tile.similar_tiles.all()]
        self.designer = TileDesignerDto(tile.design.group, language)
        self.quantity = tile.quantity_on_hand
        self.sample = tile.is_sample
        self.hasSample = tile.has_sample() 
        if self.sample:
            self.sampleId = tile.id
        else:
            self.sampleId = tile.sample.id if tile.sample else 0
        if portfolio:
            self.inPortfolio = True if portfolio.tiles.filter(tile=tile).exists() else False
        else:
            self.inPortfolio = False
        self.hasInstallationPhotos = tile.has_installation_photos()
        self.inStock = tile.in_stock
        self.price = tile.sales_price
        self.tearsheet = tile.tearsheet.url if tile.tearsheet else ''
        self.sqFt = tile.get_sq_ft()
        self.sqFtPrice = tile.get_price_by_sq_ft()
        self.qtyIsSqFt = tile.qty_is_sq_ft
        self.maximumSqFt = tile.design.group.collection.maximum_input_square_foot
        self.minimumSqFt = tile.design.group.collection.minimum_input_square_foot
        if tile.in_stock():
            self.leadTime = LeadTime.objects.get(pk=1).get_description(language)
        else:
            self.leadTime = LeadTime.objects.get(pk=2).get_description(language)
        if tile.box:
            self.box = BoxDto(tile.box)
        if tile.in_stock():
            self.shipFrom = [WarehouseDto(warehouse, language) for warehouse in
                              Warehouse.objects.filter(in_stock=True)]
        else:
            self.shipFrom = [WarehouseDto(warehouse, language) for warehouse in
                              Warehouse.objects.filter(custom=True)]

class InStockDto(BaseCatalogDto):

    def __init__(self, tile, is_sample, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.rotateDeg1 = tile.rotate_deg1
        self.rotateDeg2 = tile.rotate_deg2
        self.rotateDeg3 = tile.rotate_deg3
        self.rotateDeg4 = tile.rotate_deg4
        self.collection = tile.design.group.collection.get_title(language) \
                          if tile.design.group.collection else ''
        self.size = tile.size
        self.hasInstallationPhotos = tile.has_installation_photos()

        if is_sample == 'true':
            self.hasSample = True
        else:
            self.hasSample = True if tile.has_sample() else False
        
        if tile.is_sample:
            self.sampleId = tile.id
        else:
            self.sampleId = tile.sample.id if tile.sample else 0


class CollectionsFiltersDto(BaseDto):

    def __init__(self, collection, language):
        super().__init__(collection)
        self.title = collection.get_menu(language)


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
            self.title = collection.get_menu(language)
            self.url = collection.get_absolute_url(language)
        else:
            self.title = collection.menu_title
            self.url = collection.get_absolute_url()
        self.image = collection.menu_image.url if collection.image else ''


class BasePortfolioTilesDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.sizes = [TileSizeDto(size) for size in tile.get_available_sizes()]
        self.url = tile.get_absolute_url(language)


class PortfolioTilesDto(BasePortfolioTilesDto):

    def __init__(self, portfoliotile_id, tile, language, isCustomTile=False, colorGroups = []):
        super().__init__(tile, language)
        self.portfoliotile_id = portfoliotile_id
        self.isCustomTile = isCustomTile
        self.plane = tile.plane.url if tile.plane else ''
        if isCustomTile:
            self.colorGroups = [GroupColorDto(colorGroup, language) for colorGroup in colorGroups]
        else:
            self.colorGroups = [GroupColorDto(colorGroup, language) for colorGroup in tile.colors.all()]
            
        
        
class GroupColorDto:
    
    def __init__(self, group_color, language):
        self.group = group_color.group
        self.color = TileColorDto(group_color.color, language)      


class PortfolioCustomizedTilesDto(BasePortfolioTilesDto):

    def __init__(self, customized_tile, language):
        super().__init__(customized_tile.tile, language)
        self.customizedTileId = customized_tile.id
        self.groupColors = [GroupColorDto(color_group, language) for color_group in customized_tile.color_groups.all() ]


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
        self.image = tile.image.url if tile.image else ''
        self.size = tile.size
