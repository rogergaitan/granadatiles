from django.shortcuts import get_object_or_404
from .models import Collection, Group, Tile, Portfolio
from .dtos import (
    CollectionDto, CollectionDetailDto, GroupDto, TileDesignDto,
    MenuCollectionDto, TileStyleDto, TileDetailDto, TileInstallationPhotosDto,
    TileSizeDto, TileOrderDto, InStockDto, CollectionsFiltersDto, PortfolioDto
)

from apps.tiles.models import Style

class CollectionService:

    def get_collection(id ,language=None):
        collection = get_object_or_404(Collection, pk=id)
        collectionDto = CollectionDetailDto(collection, language)
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
        groups = collection.groups.filter(show_in_web=True)
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
        group = get_object_or_404(Group, pk=id, show_in_web=True)
        groupDto = GroupDto(group, language)
        return groupDto

    def get_group_designs(id, limit, offset, style, size, new, in_stock, special, language=None):
        group = get_object_or_404(Group, pk=id, show_in_web=True)
        designs = group.designs.filter(show_in_web=True)
        if style: group.designs.filter(styles__name=style)

        tiledesignDto = [TileDesignDto(tile_design, size, new, in_stock, special, language)
                         for tile_design in designs[offset:limit]]

        return tiledesignDto

    def get_styles(id, language=None):
        group = get_object_or_404(Group, pk=id, show_in_web=True)
        styles = Style.objects.filter(designs__group__id=id).distinct()
        styleDto = [TileStyleDto(style, language) for style in styles]
        return styleDto

    def get_sizes(id):
        group = get_object_or_404(Group, pk=id, show_in_web=True)
        designs = group.designs.filter(show_in_web=True)
        sizes = [design.tiles.values_list('size', flat=True).distinct() for design in designs]

        unique_sizes = []
        for size in sizes:
            if size[0] not in unique_sizes:
                unique_sizes.append(size[0])

        sizeDto = TileSizeDto(unique_sizes)
        return sizeDto


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

      def get_tile_order(id, language):
          tile = get_object_or_404(Tile, pk=id)
          tileorderDto = TileOrderDto(tile, language)
          return tileorderDto

      def get_in_stock_tiles(ids, is_sample, limit, offset, language):
          if ids: tiles = Tile.objects.filter(design__group__collection__in=ids)

          if is_sample:
              tiles = Tile.objects.filter(is_sample=True)
          else:
              tiles = Tile.objects.filter(is_sample=False)
          instockdto = [InStockDto(tile, language) for tile in tiles[offset:limit] if tile.design]
          return instockdto

      def get_tiles_collections_filters(language):
          collections = Collection.objects.filter(featured=True)
          collectiondto = [CollectionsFiltersDto(collection, language) for collection in collections]
          return collectiondto


class PortfolioService:

     def get_portfolio(user, language):
         portfolio = Portfolio.objects.get(user=user)
         portfoliodto = PortfolioDto(portfolio, language)
         return portfoliodto
