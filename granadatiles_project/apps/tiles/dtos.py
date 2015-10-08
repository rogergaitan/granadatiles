from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        if language:
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()


class TileSizeDto():

    def __init__(self, tile_size, language=None):
        self.name = tile_size.weight


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language=None):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.sizes = [TileSizeDto(tile_size, language) for tile_size in tile.sizes.all()]


class TileDesignDto(BaseCatalogDto):

    def __init__(self, tile_design, language=None):
        super().__init__(tile_design, language)
        self.main = TileDto(tile_design.tiles.filter(main=True)[0], language)
        self.tiles = [TileDto(tile, language) for tile in tile_design.tiles.filter(main=False)]


class GroupRetrieveDto(BaseContentDto):
    pass


class GroupDto(BaseGalleryImageDto):
    pass


class MenuCollectionDto(object):
    def __init__(self, collection, language = None):
        if language:
            self.title = collection.get_title(language)
            self.url = collection.get_absolute_url(language)
        else:
            self.title = collection.title
            self.url = collection.get_absolute_url()
        self.image = collection.menu_image
