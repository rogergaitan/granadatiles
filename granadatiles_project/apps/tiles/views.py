from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from core.views import BaseViewSet

from apps.tiles.serializers import (
    GroupSerializer, GroupDesignSerializer, MenuCollectionSerializer,
    CollectionSerializer, CollectionRetrieveSerializer, TileDesignSerializer
)
from apps.tiles.services import CollectionService, GroupService
from apps.tiles.models import Collection, Group


def collection_detail(request, slug):
    collection_id = Collection.objects.get_id(slug, request.LANGUAGE_CODE)
    return render(request, "tiles/collection_detail.html", {
        'collection_id': collection_id
    })


def group_detail(request, slug):
    collection_id = Collection.objects.get_id(slug, request.LANGUAGE_CODE)
    return render(request, "tiles/group_detail.html", {
        'collection_id': collection_id
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
   def tiles(self, request, pk = None):
       limit = int(request.query_params.get('limit', 6))
       offset = int(request.query_params.get('offset', 0))
       tile_designs = GroupService.get_group_designs(id=pk,
           language=self.get_language(request), limit=limit, offset=offset)
       serializer = TileDesignSerializer(tile_designs, many=True)
       return Response(serializer.data)
