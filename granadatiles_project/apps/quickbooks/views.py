from django.core.management import call_command

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import list_route

from .services import ItemService
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ViewSet):

    permission_classes = (IsAdminUser,)

    def list(self, request):
        items = ItemService.get_items()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @list_route()
    def update_inventory(self, request):
        call_command('update_inventory')
        return Response({'message': 'Finished task'})
