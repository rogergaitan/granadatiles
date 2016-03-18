from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.views import BaseViewSet
from core.utils import convert_to_boolean

from .serializers import (
    GroupSerializer, GroupDesignSerializer, MenuCollectionSerializer,
    CollectionSerializer, CollectionRetrieveSerializer, TileDesignSerializer,
    StyleSerializer, GroupTileSizeSerializer, TileDetailSerializer,
    TileInstallationPhotosSerializer, TileOrderSerializer, CollectionsFilterSerializer,
    InStockSerializer, PortfolioTilesSerializer, PortfolioCustomTilesSerializer, LayoutSerializer,
    LayoutTilesSerializer, CollectionInstallationPhotosSerializer, TileColorSerializer, GroupColorSerializer
)
from .services import CollectionService, GroupService, TileService, PortfolioService, PalleteColorService
from .models import Collection, Group


def collection_detail(request, slug):
    collection_id = Collection.objects.get_id(slug, request.LANGUAGE_CODE)
    return render(request, "tiles/collection_detail.html", {
        'collection_id': collection_id
    })


def group_detail(request, collection_slug, group_slug):
    collection_id = Collection.objects.get_id(collection_slug, request.LANGUAGE_CODE)
    group_id = Group.objects.get_id(group_slug, request.LANGUAGE_CODE)
    return render(request, "tiles/group_detail.html", {
        'collection_id': collection_id,
        'group_id': group_id
    })

def instock_samples(request):
    return render(request, 'tiles/instock_samples.html')

def instock_tiles(request):
    return render(request, 'tiles/instock_tiles.html')

"""
These are the views for the api
"""


class CollectionViewSet(BaseViewSet):

    # /collections/
    def list(self, request):
        collections = CollectionService.get_collections(
            language= self.get_language(request))
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)

    # /collections/:id
    def retrieve(self, request, pk=None):
        collection = CollectionService.get_collection(
                                        id=pk,
                                        language=self.get_language(request))
        serializer = CollectionRetrieveSerializer(collection)
        return Response(serializer.data)


    # /collections/:id/groups
    @detail_route(methods=['get'])
    def groups(self, request, pk=None):
        groups = CollectionService.get_groups(
                                        collection_id=pk,
                                        language=self.get_language(request))
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    # /collections/menu
    @list_route(methods=['get'])
    def menu(self, request):
        filter = request.query_params.get('exclude')
        collections = CollectionService.get_menu_collections(
            language=self.get_language(request), filter=filter)
        serializer = MenuCollectionSerializer(collections, many=True)
        return Response(serializer.data)

     # /collections/featured
    @list_route(methods=['get'])
    def featured(self, request):
        collections = CollectionService.get_featured_collections(
            language= self.get_language(request))
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def installationphotos(self, request, pk=None):
        collection = CollectionService.get_collection(pk, self.get_language(request))
        installation_photos = CollectionService.get_installation_photos(collection,
                                                                        self.get_language(request))
        serializer = CollectionInstallationPhotosSerializer(installation_photos, many=True)
        return Response(serializer.data)


class GroupViewSet(BaseViewSet):

    def retrieve(self, request, pk=None):
        group = GroupService.get_group(id=pk, language=self.get_language(request))
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def tiles(self, request, pk=None):
        limit = int(request.query_params.get('limit', 6))
        offset = int(request.query_params.get('offset', 0))
        style = request.query_params.get('style')
        size = request.query_params.get('size')
        new = convert_to_boolean(request.query_params.get('recent'))
        in_stock = convert_to_boolean(request.query_params.get('in_stock'))
        specials = convert_to_boolean(request.query_params.get('specials'))

        tile_designs = GroupService.get_group_designs(
            id=pk, language=self.get_language(request), limit=limit,
            offset=offset, style=style, size=size, new=new,
            in_stock=in_stock, specials=specials
        )

        serializer = TileDesignSerializer(tile_designs, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def styles(self, request, pk=None):
        styles = GroupService.get_styles(id=pk, language=self.get_language(request))
        serializer = StyleSerializer(styles, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def sizes(self, request, pk=None):
        sizes = GroupService.get_sizes(pk)
        serializers = GroupTileSizeSerializer(sizes)
        return Response(serializers.data)


class TileViewSet(BaseViewSet):

    def retrieve(self, request, pk=None):
        tile = TileService.get_tile(id=pk, language=self.get_language(request))
        serializer = TileDetailSerializer(tile)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def installationphotos(self, request, pk=None):
        tile = TileService.get_tile_installation_photos(id=pk, language=self.get_language(request))
        serializer = TileInstallationPhotosSerializer(tile, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def order(self, request, pk=None):
        if request.user.is_authenticated() and request.user.is_superuser == False:
            portfolio = PortfolioService.get_portfolio(request.user)
        else:
            portfolio = False
        tile = TileService.get_tile_order(id=pk,
                                          portfolio=portfolio,
                                          language=self.get_language(request))
        serializer = TileOrderSerializer(tile)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def in_stock_tiles(self, request):
        collection_filter = request.query_params.getlist('ids')
        is_sample = request.query_params.get('is_sample')
        limit = int(request.query_params.get('limit', 6))
        offset = int(request.query_params.get('offset', 0))

        tiles = TileService.get_in_stock_tiles(collection_filter, is_sample,
                                               limit, offset, self.get_language(request))
        serializer = InStockSerializer(tiles, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def collections_filters(self, request):
        collections = TileService.get_tiles_collections_filters(language=self.get_language(request))
        serializer = CollectionsFilterSerializer(collections, many=True)
        return Response(serializer.data)


class PortfolioTilesViewSet(BaseViewSet):

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        tiles = PortfolioService.show_tiles(request.user, self.get_language(request))
        serializer = PortfolioTilesSerializer(tiles, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        return Response(PortfolioService.remove_tile(request, pk))

    def create(self, request):
        id = request.data.get('id')
        return Response(PortfolioService.add_tile(request, id))

    def retrieve(self, request, pk=None):
        return Response(PortfolioService.check_tile(request, pk))


class LayoutsViewSet(BaseViewSet):

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        layouts = PortfolioService.show_layouts(request.user)
        serializer = LayoutSerializer(layouts, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        return Response(PortfolioService.get_layout(pk).delete())

    def create(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        id = request.data.get('id')
        name = request.data.get('name')
        lenght_ft = request.data.get('lenght_ft')
        lenght_in = request.data.get('lenght_in')
        width_ft = request.data.get('width_ft')
        width_in = request.data.get('width_in')
        image = request.data.get('image')
        return Response(PortfolioService.create_layout(portfolio, id, name, lenght_ft,
                                                     lenght_in, width_ft, width_in, image))

    @detail_route(methods=['post'])
    def duplicates(self, request, pk=None):
        portfolio = PortfolioService.get_portfolio(request.user)
        return Response(PortfolioService.duplicate_layout(portfolio, pk))


class CustomizedTilesViewSet(BaseViewSet):

    permission_classes = (IsAuthenticated,)

    @detail_route(methods=['get'])
    def groupcolors(self, request, pk=None):
        portfolio = PortfolioService.get_portfolio(request.user)
        group_colors = PortfolioService.get_group_colors(portfolio, pk, self.get_language(request))
        serializer = GroupColorSerializer(group_colors, many=True)
        return Response(serializer.data)
    
    @detail_route(methods=['post'])
    def groupcolors(self, request, pk=None):
        color_id = request.data.get('colorId')
        group = request.data.get('group')
        return Response(PortfolioService.add_custom_tile_color(pk, group, color_id))

    def destroy(self, request, pk=None):
        portfolio = PortfolioService.get_portfolio(request.user)
        return Response(PortfolioService.remove_custom_tile(portfolio, pk))

    def create(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        tile = PortfolioService.get_tile(request.data.get('id'))
        return Response(PortfolioService.add_custom_tile(portfolio, tile))


class PalleteColorsViewSet(BaseViewSet):

    def list(self, request):
        pallete_colors = PalleteColorService.get_pallete_colors(self.get_language(request))
        serializer = TileColorSerializer(pallete_colors, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ViewSet):

    permission_classes = (IsAdminUser,)

    @list_route(methods=['post'])
    def update_inventory(self, request):
        update_inventory_task.delay()
        return Response({'message': 'Finished task'})
