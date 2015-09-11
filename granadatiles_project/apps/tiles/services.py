from apps.tiles.models import Collection
from apps.tiles.dtos import CollectionDto, GroupDto


class CollectionService(object):

    def get_collection(id ,language=None):
        collection = Collection.objects.get(pk=id)
        collectionDto = CollectionDto(collection, language)
        return collectionDto

    def get_collections(language=None):
        collections = Collection.objects.all()
        collectionsDto = [CollectionDto(collection, language=language)
                          for collection in collections]
        return collectionsDto

    def get_groups(collection_id, language=None):
        groups = Collection.objects.get(pk=collection_id).groups.all()
        groupsDto = [GroupDto(group, language) 
                     for group in groups]
        return groupsDto
