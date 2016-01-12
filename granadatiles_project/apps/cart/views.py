from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, detail_route

from core.views import BaseViewSet
from apps.tiles.models import Tile
from .services import CartService
from .serializers import TileOrdersSerializer, SampleOrdersSerializer, CustomizedTileOrdersSerializer


class CartViewSet(BaseViewSet):

    @list_route(methods=['get'])
    def tiles_count(self, request):
        cart = CartService.get_cart(request)
        tiles_count = cart.tile_orders.count() + cart.sample_orders.count()
        return Response({'count': tiles_count})

    @list_route(methods=['get'])
    def show_tile_orders(self, request):
        cart = CartService.get_cart(request)
        tile_orders = CartService.get_tile_orders(cart, self.get_language(request))
        serializer = TileOrdersSerializer(tile_orders, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def add_tile(self, request):
        cart = CartService.get_cart(request)
        tile = CartService.get_tile(request.query_params.get('id'))
        sq_ft = int(request.query_params.get('sq_ft'))
        return Response(CartService.add_tile(cart, tile, sq_ft))

    @list_route(methods=['get'])
    def show_customized_tile_orders(self, request):
        cart = CartService.get_cart(request)
        customized_tile_orders = CartService.get_customized_tile_orders(cart, self.get_language(request))
        serializer = CustomizedTileOrdersSerializer(customized_tile_orders, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def add_custom_tile(self, request):
        cart = CartService.get_cart(request)
        tile = CartService.get_tile(request.query_params.get('id'))
        return Response(CartViewSet.add_custom_tile(cart, tile))

    @list_route(methods=['get'])
    def remove_tile(self, request):
        cart = CartService.get_cart(request)
        id = request.query_params.get('id')
        return Response(CartService.remove_tile(cart, id))

    @list_route(methods=['get'])
    def show_sample_orders(self, request):
        cart = CartService.get_cart(request)
        sampleorders = CartService.get_sample_orders(cart, language=self.get_language(request))
        serializer = SampleOrdersSerializer(sampleorders, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def add_sample(self, request):
        cart = CartService.get_cart(request)
        id = request.query_params.get('id')
        quantity = request.query_params.get('quantity')
        return Response(CartService.add_sample(cart, id, quantity))

    @list_route(methods=['get'])
    def remove_sample(self, request):
        cart = CartService.get_cart(request)
        id = request.query_params.get('id')
        return Response(CartService.remove_sample(cart, id))
