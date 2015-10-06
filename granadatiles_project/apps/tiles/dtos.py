from core.dtos import BaseGalleryImageDto, BaseContentDto, BaseCatalogDto


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        if language:
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()


class TileDto(BaseCatalogDto):
    pass


class TileDesignDto(BaseCatalogDto):

    def __init__(self, tile_design, language=None):
        super().__init__(tile_design, language)
        self.tiles = tile_design.tiles.all()


class GroupDto(BaseGalleryImageDto):
    pass


class GroupDesignDto(GroupDto):

   def __init__(self, group, offset, limit, language=None):
       	super().__init__(group, language)
        self.designs = [TileDesignDto(tile, language) for tile in group.designs.all()[offset:limit + 1]]


class MenuCollectionDto(object):
    def __init__(self, collection, language = None):
        if language:
            self.title = collection.get_title(language)
            self.url = collection.get_absolute_url(language)
        else:
            self.title = collection.title
            self.url = collection.get_absolute_url()
        self.image = collection.menu_thumbnail
