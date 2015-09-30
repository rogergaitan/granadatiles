from apps.tiles.models import Collection, Group
from apps.tiles.dtos import CollectionDto, GroupDto, GroupTileDto, MenuCollectionDto


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

    def get_featured_collections(language=None):
        collections = Collection.objects.filter(featured=True)
        collectionsDto = [CollectionDto(collection, language=language)
                          for collection in collections]
        return collectionsDto

    def get_groups(collection_id, language=None):
        groups = Collection.objects.get(pk=collection_id).groups.all()
        groupsDto = [GroupDto(group, language) 
                     for group in groups]
        return groupsDto

    def get_menu_collections(language = None):
        collections = Collection.objects.filter(show_in_menu=True)
        menuCollectionsDto = [MenuCollectionDto(collection, language = language)
                              for collection in collections]
        return menuCollectionsDto
	

class GroupService(object):
	
    def get_group(id, language=None):
       group = Group.objects.get(pk=id)
       grouptileDto = GroupTileDto(group, language)
       return grouptileDto