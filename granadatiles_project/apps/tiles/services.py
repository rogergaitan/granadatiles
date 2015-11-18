from django.shortcuts import get_object_or_404
from .models import Collection, Group, Tile
from .dtos import (
    CollectionDto, CollectionRetrieveDto, GroupDto,
    TileDesignDto, MenuCollectionDto, TileStyleDto, TileDetailDto,
    TileInstallationPhotosDto
)


class CollectionService:

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


class GroupService:

    def get_group(id, language=None):
        group = get_object_or_404(Group, pk=id)
        groupDto = GroupDto(group, language)
        return groupDto

    def get_group_designs(id, limit, offset, style, size, language=None):
        group = get_object_or_404(Group, pk=id)
        design = group.designs.filter(styles__name=style) if style else group.designs.all()

        tiledesignDto = [TileDesignDto(tile_design, size, language) for tile_design in design[offset:limit + 1]]

        return tiledesignDto

    def get_styles(id, language=None):
        group = get_object_or_404(Group, pk=id)
        styleDto = [TileStyleDto(style, language) for style in group.styles.all()]
        return styleDto


class TileService:

      def get_tile(id, language):
          tile = get_object_or_404(Tile, pk=id)
          tiledetailDto = TileDetailDto(tile, language)
          return tiledetailDto

      def get_tile_installation_photos(id, language):
          tile = get_object_or_404(Tile, pk=id)
          if tile.installation_photos.exists():
              tileinstallationphotosDto = [TileInstallationPhotosDto(photo, language)
                                           for photo in tile.installation_photos.all()]
          else: tileinstallationphotosDto = None
          return tileinstallationphotosDto
