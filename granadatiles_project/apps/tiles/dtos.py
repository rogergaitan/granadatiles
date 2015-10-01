from core.dtos import BaseGalleryImageDto, BaseContentDto


class CollectionDto(BaseGalleryImageDto):

    def __init__(self, collection, language=None):
        super().__init__(collection, language)
        if language:
            self.url = collection.get_absolute_url(language)
        else:
            self.url = collection.get_absolute_url()


class TileDto(BaseContentDto):
    pass


class GroupDto(BaseGalleryImageDto):
    pass


class GroupTileDto(GroupDto):

   def __init__(self, group, offset, limit, language=None):
       	super().__init__(group, language)
        self.tiles = [TileDto(tile, language) for tile in group.tiles.all()[offset:limit + 1]]


class MenuCollectionDto(object):
    def __init__(self, collection, language = None):
        if language:
            self.title = collection.get_title(language)
            self.url = collection.get_absolute_url(language)
        else:
            self.title = collection.title
            self.url = collection.get_absolute_url()
        self.image = collection.menu_thumbnail
