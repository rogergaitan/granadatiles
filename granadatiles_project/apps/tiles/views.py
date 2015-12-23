from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAdminUser

from core.views import BaseViewSet

from .serializers import (
    GroupSerializer, GroupDesignSerializer, MenuCollectionSerializer,
    CollectionSerializer, CollectionRetrieveSerializer, TileDesignSerializer,
    StyleSerializer, GroupTileSizeSerializer, TileDetailSerializer,
    TileInstallationPhotosSerializer, TileOrderSerializer, CollectionsFilterSerializer,
    InStockSerializer, PortfolioTilesSerializer, LayoutSerializer
)
from .services import CollectionService, GroupService, TileService, PortfolioService
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
    def groups(self, request, pk = None):
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


class GroupViewSet(BaseViewSet):

    def retrieve(self, request, pk=None):
        group = GroupService.get_group(id=pk, language=self.get_language(request))
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def tiles(self, request, pk=None):
        limit = int(request.query_params.get('limit', 6))
        offset = int(request.query_params.get('offset', 0))
        style = request.query_params.get('style', None)
        size = request.query_params.get('size', None)
        new = request.query_params.get('new', None)
        in_stock = request.query_params.get('in_stock', None)
        special = request.query_params.get('special', None)

        tile_designs = GroupService.get_group_designs(
            id=pk, language=self.get_language(request), limit=limit,
            offset=offset, style=style, size=size, new=new,
            in_stock=in_stock, special=special
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
        tile = TileService.get_tile_order(id=pk, language=self.get_language(request))
        serializer = TileOrderSerializer(tile)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def in_stock_tiles(self, request):
        collection_filter = request.query_params.getlist('ids')
        is_sample = request.query_params.get('is_sample')
        limit = int(request.query_params.get('limit', 6))
        offset = int(request.query_params.get('offset', 0))

        tiles = TileService.get_in_stock_tiles(collection_filter, is_sample,
                                               limit, offset, language=self.get_language(request))
        serializer = InStockSerializer(tiles, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def collections_filters(self, request):
        collections = TileService.get_tiles_collections_filters(language=self.get_language(request))
        serializer = CollectionsFilterSerializer(collections, many=True)
        return Response(serializer.data)


class PortfolioViewSet(BaseViewSet):

    @list_route(methods=['get'])
    def show_tiles(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        tiles = PortfolioService.show_tiles(portfolio, self.get_language(request))
        serializer = PortfolioTilesSerializer(tiles, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def remove_tile(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        id = request.query_params.get('id')
        return Response(PortfolioService.remove_tile(portfolio, id))

    @list_route(methods=['get'])
    def add_tile(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        id = request.query_params.get('id')
        return Response(PortfolioService.add_tile(portfolio, id))


    @list_route(methods=['get'])
    def show_layouts(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        layouts = PortfolioService.show_layouts(portfolio)
        serializer = LayoutSerializer(layouts, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def remove_layout(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        id = request.query_params.get('id')
        return Response(PortfolioService.remove_layout(portfolio, id))

    @list_route(methods=['post'])
    def create_layout(self, request):
        portfolio = PortfolioService.get_portfolio(request.user)
        name = request.query_params.post('name')
        lenght_ft = request.query_params.post('lenght_ft')
        lenght_in = request.query_params.post('lenght_in')
        width_ft = request.query_params.post('width_ft')
        width_in = request.query_params.post('width_in')
        return Response(PortfolioService.create_layout(portfolio, name, lenght_ft,
                                                       lenght_in, width_ft, width_in))


class ItemViewSet(viewsets.ViewSet):

    permission_classes = (IsAdminUser,)


    @list_route(methods=['post'])
    def update_inventory(self, request):
        update_inventory_task.delay()
        return Response({'message': 'Finished task'})
