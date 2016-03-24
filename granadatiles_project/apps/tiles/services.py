from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

from .models import (
    Collection, Group, Tile, Portfolio, Layout, Style,
    CustomizedTile, GroupColor, PalleteColor, PortfolioTile
)
from .dtos import (
    CollectionDto, CollectionDetailDto, GroupDto, TileDesignDto,
    MenuCollectionDto, TileStyleDto, TileDetailDto, TileInstallationPhotosDto,
    TileSizeDto, TileOrderDto, InStockDto, CollectionsFiltersDto, PortfolioTilesDto,
    LayoutDto, LayoutTilesDto, PortfolioCustomizedTilesDto, CollectionInstallationPhotosDto,
    TileColorDto, GroupColorDto
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

    def get_installation_photos(collection, language):
        tiles = Tile.objects.filter(design__group__collection=collection.id)

        #filter unique gallery images
        filter_photos = {photo for tile in tiles for photo in tile.installation_photos.all()}
        installation_photos_dto = [CollectionInstallationPhotosDto(photo, language)
                                   for photo in filter_photos]
        return installation_photos_dto


class GroupService:

    def group_show_in_web(id):
        return get_object_or_404(Group, pk=id, show_in_web=True)

    def get_group(id, language=None):
        group = GroupService.group_show_in_web(id)
        group_dto = GroupDto(group, language)
        return group_dto

    def get_group_designs(id, limit, offset, style, size, new, in_stock, specials, language=None):
        group = GroupService.group_show_in_web(id)
        designs = group.designs.filter(show_in_web=True)

        if style != '0': designs = designs.filter(styles__id=style)

        if new: designs = designs.filter(tiles__new=True).distinct()

        if in_stock: designs = designs.filter(tiles__custom=False).distinct()

        if specials: designs = designs.filter(tiles__on_sale=True).distinct()

        tile_design_dto = [TileDesignDto(tile_design, size, new, in_stock, specials, language)
                           for tile_design in designs[offset:(limit+offset)]]
        return tile_design_dto

    def get_styles(id, language=None):
        group = GroupService.group_show_in_web(id)
        styles = Style.objects.filter(designs__group__id=id).distinct()
        style_dto = [TileStyleDto(style, language) for style in styles]
        return style_dto

    def get_sizes(id):
        group = GroupService.group_show_in_web(id)
        designs = group.designs.filter(show_in_web=True)
        sizes = [design.tiles.values_list('size', flat=True).distinct() for design in designs]

        unique_sizes = []
        for size in sizes:
            if size[0] not in unique_sizes:
                unique_sizes.append(size[0])

        size_dto = TileSizeDto(unique_sizes)
        return size_dto


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

    def get_tile_order(id, portfolio, language):
        tile = get_object_or_404(Tile.objects.select_related('box','sample', 'design'), pk=id)
        tileorderDto = TileOrderDto(tile, portfolio, language)
        return tileorderDto

    def get_in_stock_tiles(ids, is_sample, limit, offset, language):

        if ids:
            tiles = Tile.objects.filter(design__group__collection__id__in=ids)
        else:
            tiles = Tile.objects.all()

        if is_sample == 'true':
            tiles = tiles.filter(is_sample=True).order_by('name')
        elif is_sample == 'false' or is_sample is None:
            tiles = tiles.filter(is_sample=False).order_by('name')

        instock_dto = [InStockDto(tile, is_sample, language)
                        for tile in tiles[offset:(limit+offset)]
                        if tile.design]
        return instock_dto

    def get_tiles_collections_filters(language):
        collections = Collection.objects.filter(featured=True)
        collectiondto = [CollectionsFiltersDto(collection, language) for collection in collections]
        return collectiondto


class PortfolioService:

    def get_tile(id):
        return get_object_or_404(Tile, pk=id)

    def get_portfolio(user):
        return get_object_or_404(Portfolio, user=user)

    def get_portfolio_tile(id):
        return get_object_or_404(PortfolioTile, pk=id)

    def get_customized_tile(id):
        return get_object_or_404(CustomizedTile, pk=id)

    def get_layout(id):
        return get_object_or_404(Layout, pk=id)

    def show_tiles(user, language):
        portfolio = PortfolioService.get_portfolio(user)
        portfolio_tiles_dto = [PortfolioTilesDto(portfolio_tile.id, portfolio_tile.tile, language)
                                for portfolio_tile in portfolio.tiles.all()]
        portfolio_tiles_dto += [PortfolioTilesDto(portfolio_tile.id, portfolio_tile.tile, language, isCustomTile=True, colorGroups=portfolio_tile.color_groups.all())
                                for portfolio_tile in portfolio.customized_tiles.all()]
        return portfolio_tiles_dto

    def remove_tile(request, id):
        portfolio = PortfolioService.get_portfolio(request.user)
        if request.query_params.get('isCustomTile', False):
            CustomizedTile.objects.get(pk=id).delete()
        else:
            portfolio.tiles.get(pk=id).delete()

    def add_tile(request, id):
        portfolio = PortfolioService.get_portfolio(request.user)
        tile = PortfolioService.get_tile(id)
        portfolio.tiles.create(tile=tile)

    def show_layouts(user):
        portfolio = PortfolioService.get_portfolio(user)
        layouts_dto = [LayoutDto(layout) for layout in portfolio.layouts.all()]
        return layouts_dto

    def create_layout(portfolio, id, name, length_ft, length_in, width_ft, width_in, image):
        data = {
            'name': name,
            'length_ft': length_ft,
            'length_in': length_in,
            'width_ft': width_ft,
            'width_in': width_in,
            'image': image
        }
        portfolio.layouts.update_or_create(pk=id, defaults=data)

    def layout_tiles(portfolio, language):
        layout_tiles_dto = [LayoutTilesDto(portfolio_tile.tile, language)
                             for portfolio_tile in portfolio.tiles.all()]
        return layout_tiles_dto

    def duplicate_layout(portfolio, id):
        layout = Layout.objects.get(pk=id)
        layout.id = None
        layout.name = layout.name + ' ' + _('copy')
        layout.save()

    def show_customized_tiles(portfolio, language):
        customized_tiles_dto = [PortfolioCustomTilesDto(custom_tile.id, custom_tile.tile, language)
                              for customtile in portfolio.customized_tiles.all()]
        return customized_tiles_dto

    def show_customized_tile(id, language):
        customized_tile = PortfolioService.get_customized_tile(id)
        customized_tile_dto = PortfolioCustomizedTilesDto(customized_tile, language)
        return customized_tile_dto

    def update_or_create_customized_tile(customized_tile, color_groups):
        for color_group in color_groups:
            color = get_object_or_404(PalleteColor, pk=color_group['colorId'])
            data = {'color':color}

            GroupColor.objects.update_or_create(
                customized_tile=customized_tile,
                group= color_group['group'],
                defaults=data
            )
        return {'customizedTileId': customized_tile.id, 'colorGroups': color_groups}

    def add_customized_tile(request, tile_id, color_groups):
        portfolio = PortfolioService.get_portfolio(request.user)
        tile = PortfolioService.get_tile(tile_id)
        customized_tile = CustomizedTile.objects.create(tile=tile, portfolio=portfolio)

        return PortfolioService.update_or_create_customized_tile(customized_tile, color_groups)

    def remove_customized_tile(portfolio, customizedtile_id):
        portfolio.customized_tiles.get(pk=customizedtile_id).delete()

    def update_customized_tile(request, customized_tile_id, color_groups):
        portfolio = PortfolioService.get_portfolio(request.user)
        customized_tile = PortfolioService.get_customized_tile(customized_tile_id)

        return PortfolioService.update_or_create_customized_tile(customized_tile, color_groups)


class PalleteColorService:

    def get_pallete_colors(language):
        pallete_colors_dto = [TileColorDto(pallete_color, language) for pallete_color in PalleteColor.objects.all()]
        return pallete_colors_dto
