from django.shortcuts import get_object_or_404
from .models import Collection, Group, Tile, Portfolio, Layout, Style, CustomizedTile
from .dtos import (
    CollectionDto, CollectionDetailDto, GroupDto, TileDesignDto,
    MenuCollectionDto, TileStyleDto, TileDetailDto, TileInstallationPhotosDto,
    TileSizeDto, TileOrderDto, InStockDto, CollectionsFiltersDto, PortfolioTilesDto,
    LayoutDto, LayoutTilesDto
)

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

     def get_tile(id):
         return get_object_or_404(Tile, list_id=id)

     def get_portfolio(user):
         return get_object_or_404(Portfolio, user=user)

     def show_tiles(portfolio, language):
         portfoliotilesdto = [PortfolioTilesDto(portfoliotile.tile, language)
                              for portfoliotile in portfolio.tiles.all()]
         return portfoliotilesdto

     def remove_tile(portfolio, id):
         tile = PortfolioService.get_tile(id)
         portfolio.tiles.get(tile=tile).delete()

     def add_tile(portfolio, id):
         tile = PortfolioService.get_tile(id)
         portfolio.tiles.create(tile=tile)

     def show_layouts(portfolio):
         layoutsdto = [LayoutDto(layout) for layout in portfolio.layouts.all()]
         return layoutsdto

     def remove_layout(portfolio, id):
         layout = get_object_or_404(Layout, pk=id)
         portfolio.layouts.get(pk=layout.id).delete()

     def save_layout(portfolio, id, name, length_ft, length_in, width_ft, width_in, image):
         if id:
             layout = get_object_or_404(Layout, pk=id)
             layout.update(name=name, length_ft=length_ft, length_in=length_in,
                           width_ft=width_ft, width_in=width_in, image=image)
         else:
             portfolio.layouts.create(name=name, length_ft=length_ft, length_in=length_in,
                                      width_ft=width_ft, width_in=width_in, image=image)

     def layout_tiles(portfolio, language):
         layouttilesdto = [LayoutTilesDto(portfoliotile.tile, language) for portfoliotile in portfolio.tiles.all()]
         return layouttilesdto

     def duplicate_layout(portfolio, id):
         layout = Layout.objects.get(pk=id)
         layout.id = None
         layout.name = layout.name + " copy"
         layout.save()

    def save_custom_tiles(portfolio, tile, colors):
        customized_tile = CustomizedTile.objects.create(tile=tile, portfolio=portfolio)
        customized_tile.colors.add(colors)
        customized_tile.save()
