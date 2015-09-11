from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollectionSerializer
from rest_framework.response import Response
from apps.tiles.services import CollectionService
from rest_framework.decorators import list_route, detail_route
from apps.tiles.serializers import GroupSerializer


def collection_detail(request, slug):
    collection_id = Collection.objects.get_id(slug, request.LANGUAGE_CODE)
    return render(request, "tiles/collection_detail.html", {
        'collection_id': collection_id
    })


"""
Theses are the views for the api
"""


class CollectionViewSet(viewsets.ViewSet):

    # /collections
    def list(self, request):
        collections = CollectionService.get_collections(
            language=request.LANGUAGE_CODE)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)

    # /collections/:id
    def retrieve(self, request, pk=None):
        collection = CollectionService.get_collection(id=pk, 
                                                      language=request.LANGUAGE_CODE)
        serializer = GroupSerializer(collection)
        return Response(serializer.data)


    # /collections/:id/groups
    @detail_route(methods=['get'])
    def groups(self, request, pk = None):
        groups = CollectionService.get_groups(collection_id=pk,
                                              language=request.LANGUAGE_CODE)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
