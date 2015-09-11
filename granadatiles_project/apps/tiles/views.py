from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollectionSerializer
from rest_framework.response import Response
from apps.tiles.services import CollectionService


def collection_detail(request, slug):
    collection_id = Collection.objects.get_id(slug, request.LANGUAGE_CODE)
    return render(request, "tiles/collection_detail.html", {
        'collection_id': collection_id
    })


"""
Theses are the views for the api
"""


class CollectionViewSet(viewsets.ViewSet):

    def list(self, request):
        collections = CollectionService.get_collections(
            language=request.LANGUAGE_CODE)
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
