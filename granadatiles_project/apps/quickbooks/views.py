from rest_framework import viewsets
from rest_framework.response import Response

from .services import ItemService
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ViewSet):

    def list(self, request):
        items = ItemService.get_items()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
