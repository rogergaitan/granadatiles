from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        self.menu_image = collection.menu_image
        if language:
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()

class CollectionRetrieveDto(CollectionDto):

    def __init__(self, collection, language):
        super().__init__(collection, language)
        if language:
           self.introduction = collection.get_introduction(language)
        else:
           self.introduction = collection.introduction


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
        self.main = TileDto(tile_design.tiles.filter(main=True).first(), language) \
                    if tile_design.tiles.count() > 0 else None
        self.tiles = [TileDto(tile, language) for tile in tile_design.tiles.filter(main=False)]


class TileStyleDto(BaseCatalogDto):
    pass


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
