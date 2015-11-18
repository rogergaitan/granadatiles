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
        self.mosaic = tile.mosaic


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language=None):
        super().__init__(tile, language)
        self.image = tile.image.url if tile.image else ''
        self.sizes = tile.size


class TileDesignDto(BaseCatalogDto):

    def __init__(self, tile_design, size, language=None):

        tiles_filter = tile_design.tiles.filter(sizes__weight=size) if size else tile_design.tiles.all()

        super().__init__(tile_design, language)
        self.main = TileDto(tiles_filter.filter(main=True).first(), language) \
                    if tiles_filter.filter(main=True).count() > 0 else None
        self.tiles = [TileDto(tile, language) for tile in tiles_filter.filter(main=False)]


class TileStyleDto(BaseCatalogDto):
    pass


class TileInstallationPhotosDto(BaseContentDto):

    def __init__(self, photo, language):
        super().__init__(photo, language)
        self.image = photo.image


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
