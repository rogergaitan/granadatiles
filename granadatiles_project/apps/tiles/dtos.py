from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        self.menu_image = collection.menu_image
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


class MinorTileDto(TileDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''


class TileDesignDto(BaseCatalogDto):

    def __init__(self, tile_design, size, new, in_stock, special, language=None):

        tiles_filter = tile_design.tiles.exclude(image='')
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


class TileOrderDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image
        self.mosaic = tile.mosaic
        self.sizes = tile.size
        self.thickness = tile.thickness
        self.weight = tile.weight
        self.colors = [color for color in tile.colors.all()]
        self.uses = [use for use in tile.design.group.collection.uses.all()]
        self.styles = [style for style in tile.design.styles.all()]


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
        self.image = collection.menu_image
