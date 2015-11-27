from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto


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


class TileDetailDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.sizes = tile.size
        self.mosaic = tile.mosaic.url if tile.mosaic else ''


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language=None):
        super().__init__(tile, language)
        self.sizes = tile.size


class MainTileDto(TileDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.mosaic.url if tile.mosaic else ''
        self.sizes = tile.get_available_sizes()


class MinorTileDto(TileDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''


class TileDesignDto(BaseCatalogDto):

    def __init__(self, tile_design, size, new, in_stock, special, language=None):

        tiles_filter = tile_design.tiles.exclude(image='').exclude(mosaic='')
        if size: tiles_filter = tiles_filter.filter(size=size)
        if new: tiles_filter = tiles_filter.filter(new=True)
        if in_stock: tiles_filter = tiles_filter.filter(quantity_on_hand__gt=0)
        if special: tiles_filter = tiles_filter.filter(on_sale=True)

        super().__init__(tile_design, language)
        self.main = MainTileDto(tiles_filter.filter(main=True).first(), language) \
                    if tiles_filter.filter(main=True).exists() else None

        self.tiles = [MinorTileDto(tile, language) for tile in tiles_filter.filter(main=False)]


class TileStyleDto(BaseCatalogDto):
    pass


class TileSizeDto:

    def __init__(self, sizes):
        self.sizes = [size for size in sizes]


class TileInstallationPhotosDto(BaseContentDto):

    def __init__(self, photo, language):
        super().__init__(photo, language)
        self.image = photo.image


class SimilarTileDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)


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


class TileOrderDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image
        self.mosaic = tile.mosaic
        self.sizes = tile.get_available_sizes()
        self.thickness = tile.thickness
        self.weight = tile.weight
        self.colors = [TileColorDto(color, language) for color in tile.colors.all()]
        self.uses = [TileUseDto(use, language) for use in tile.design.group.collection.uses.all()]
        self.styles = [TileStyleDto(style, language) for style in tile.design.styles.all()]
        self.similar_tiles = [SimilarTileDto(tile, language) for tile in tile.similar_tiles.all()]
        self.designer = TileDesignerDto(tile.design.group, language)


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
