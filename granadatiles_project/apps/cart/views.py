from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, detail_route

from core.views import BaseViewSet
from apps.tiles.models import Tile
from .services import CartService, OrdersService
from .serializers import (
  TileOrdersSerializer, SampleOrdersSerializer, CustomizedTileOrdersSerializer,
  CustomizedSampleOrdersSerializer
)


class TileOrdersViewSet(BaseViewSet):
    
    def list(self, request):
        cart = CartService.get_cart(request)
        tile_orders = OrdersService.get_tile_orders(cart, self.get_language(request))
        serializer = TileOrdersSerializer(tile_orders, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(request.data.get('id'))
        sq_ft = int(request.data.get('sq_ft'))
        return Response(OrdersService.add_tile(cart, tile, sq_ft))
      
    def update(self, request, pk=None):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(pk)
        sq_ft = int(request.data.get('sq_ft'))
        return Response(OrdersService.update_tile(cart, tile, sq_ft))
      
    def destroy(self, request, pk=None):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(pk)
        return Response(OrdersService.remove_tile(cart, tile))
      
class TilesCountViewSet(BaseViewSet):
  
    def list(self, request):
        cart = CartService.get_cart(request)
        tiles_count = cart.tile_orders.count() + cart.sample_orders.count()
        return Response({'count': tiles_count})
    