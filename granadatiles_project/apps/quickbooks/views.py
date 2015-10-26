from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import detail_route, list_route

from .services import ItemService
from .serializers import ItemSerializer
from .tasks import update_inventory_task

class ItemViewSet(viewsets.ViewSet):

    permission_classes = (IsAdminUser,)

    def list(self, request):
        items = ItemService.get_items()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @list_route(methods=['post'])
    def update_inventory(self, request):
        update_inventory_task.delay()
        return Response({'message': 'Finished task'})
