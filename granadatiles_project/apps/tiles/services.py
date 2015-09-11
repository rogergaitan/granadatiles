from apps.tiles.models import Collection
from apps.tiles.dtos import CollectionDto


class CollectionService(object):

    def get_collections(language=None):
        collections = Collection.objects.all()
        collectionsDto = [CollectionDto(collection, language=language)
                          for collection in collections]
        return collectionsDto
