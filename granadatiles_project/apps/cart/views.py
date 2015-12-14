from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, detail_route

from core.views import BaseViewSet
from apps.tiles.models import Tile
from .services import CartService
from .serializers import TileOrdersSerializer, SampleOrdersSerializer


class CartViewSet(BaseViewSet):

    @list_route(methods=['get'])
    def tiles_count(self, request):
        cart = CartService.get_cart(request)
        tiles_count = cart.tile_orders.count() + cart.sample_orders.count()
        return Response({'count': tiles_count})

    @list_route(methods=['get'])
    def show_tile_orders(self, request):
        cart = CartService.get_cart(request)
        tileorders = CartService.get_tile_orders(cart, language=self.get_language(request))
        serializer = TileOrdersSerializer(tileorders, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def add_tile(self, request):
        cart = CartService.get_cart(request)
        id = request.query_params.get('id')
        sq_ft = int(request.query_params.get('sq_ft'))
        return Response(CartService.add_tile(cart, id, sq_ft),
                        status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def remove_tile(self, request):
        cart = CartService.get_cart(request)
        id = request.query_params.get('id')
        CartService.remove_tile(cart, id)
        return Response(status=status.HTTP_200_OK)

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
        CartService.add_sample(cart, id, quantity)
        return Response(status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def remove_sample(self, request):
        cart = CartService.get_cart(request)
        id = request.query_params.get('id')
        CartService.remove_sample(cart, id)
        return Response(status=status.HTTP_200_OK)
