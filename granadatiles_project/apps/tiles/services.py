from django.shortcuts import get_object_or_404
from .models import Collection, Group
from .dtos import (
    CollectionDto, CollectionRetrieveDto, GroupDto,
    TileDesignDto, MenuCollectionDto, TileStyleDto)


class CollectionService(object):

    def get_collection(id ,language=None):
        collection = get_object_or_404(Collection, pk=id)
        collectionDto = CollectionRetrieveDto(collection, language)
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

    def get_menu_collections(language=None, filter=None):
        collections = Collection.objects.filter(show_in_menu=True)
        if filter: collections = collections.exclude(pk=filter)
        menuCollectionsDto = [MenuCollectionDto(collection, language = language)
                              for collection in collections]
        return menuCollectionsDto


class GroupService(object):

    def get_group(id, language=None):
        group = get_object_or_404(Group, pk=id)
        groupDto = GroupDto(group, language)
        return groupDto

    def get_group_designs(id, limit, offset, language=None):
        group = get_object_or_404(Group, pk=id)
        tiledesignDto = [TileDesignDto(tile_design, language)
                         for tile_design in group.designs.all()[offset:limit + 1]]
        return tiledesignDto

    def get_styles(id, language=None):
        group = get_object_or_404(Group, pk=id)
        styleDto = [TileStyleDto(style, language) for style in group.styles.all()]
        return styleDto
