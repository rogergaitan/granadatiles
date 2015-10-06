from django.shortcuts import get_object_or_404
from apps.tiles.models import Collection, Group
from apps.tiles.dtos import CollectionDto, GroupDto, GroupDesignDto, MenuCollectionDto


class CollectionService(object):

    def get_collection(id ,language=None):
        collection = get_object_or_404(Collection, pk=id)
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
        collection = get_object_or_404(Collection, pk=collection_id)
        groups = collection.groups.all()
        groupsDto = [GroupDto(group, language)
                     for group in groups]
        return groupsDto

    def get_menu_collections(language = None):
        collections = Collection.objects.filter(show_in_menu=True)
        menuCollectionsDto = [MenuCollectionDto(collection, language = language)
                              for collection in collections]
        return menuCollectionsDto


class GroupService(object):

    def get_group_tiles(id, offset, limit, language=None):
       group = get_object_or_404(Group, pk=id)
       grouptileDto = GroupDesignDto(group, offset, limit, language)
       return grouptileDto
