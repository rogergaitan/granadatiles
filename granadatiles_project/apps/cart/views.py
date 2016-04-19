from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, detail_route
from rest_framework.decorators import api_view

from core.views import BaseViewSet
from apps.tiles.models import Tile
from .services import CartService, OrdersService
from .serializers import (
  TileOrdersSerializer, SampleOrdersSerializer, CustomizedTileOrdersSerializer,
  CustomizedSampleOrdersSerializer, BaseTileOrdersSerializer, BaseSampleOrdersSerializer
)

def cart_home(request):
    return render(request, 'cart/cart.html', {})

def checkout_home(request):
    return render(request, 'cart/checkout.html',{})


class TileOrdersViewSet(BaseViewSet):
    
    def list(self, request):
        cart = CartService.get_cart(request)
        tile_orders = OrdersService.get_tile_orders(cart, self.get_language(request))
        serializer = TileOrdersSerializer(tile_orders, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        tile_id = request.data.get('id')
        sq_ft = request.data.get('sqFt')
        return Response(OrdersService.add_tile_order(request, tile_id, sq_ft))
      
    def update(self, request, pk=None):
        sq_ft = request.data.get('sqFt')
        serializer = BaseTileOrdersSerializer(OrdersService.update_tile_order(pk, sq_ft))
        return Response(serializer.data)
      
    def destroy(self, request, pk=None):
        return Response(OrdersService.remove_tile_order(pk))
    
    
class CustomizedTileOrdersViewSet(BaseViewSet):
    
    def list(self, request):
        cart = CartService.get_cart(request)
        customized_tile_orders = OrdersService.get_customized_tile_orders(cart, self.get_language(request))
        serializer = CustomizedTileOrdersSerializer(customized_tile_orders, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        customized_tile_id = request.data.get('customizedTileId')
        sq_ft = request.data.get('sqFt')
        return Response(OrdersService.add_customized_tile(request, customized_tile_id, sq_ft))
    
    def update(self, request, pk=None):
        sq_ft = request.data.get('sqFt')
        serializer = BaseTileOrdersSerializer(OrdersService.update_customized_tile_order(pk, sq_ft))
        return Response(serializer.data)
        
    def destroy(self, request, pk=None):
        return Response(OrdersService.remove_customized_tile_order(pk))
      
      
class SampleOrdersViewSet(BaseViewSet):
    
    def list(self, request):
        cart = CartService.get_cart(request)
        sampleorders = OrdersService.get_sample_orders(cart, language=self.get_language(request))
        serializer = SampleOrdersSerializer(sampleorders, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(request.data.get('id'))
        quantity = request.data.get('quantity')
        return Response(OrdersService.add_sample(cart, tile, quantity))
      
    def update(self, request, pk=None):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(pk)
        quantity = request.data.get('quantity')
        serializer = BaseSampleOrdersSerializer(OrdersService.update_sample(cart, tile, quantity))
        return Response(serializer.data)
        
    def destroy(self, request, pk=None):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(pk)
        return Response(OrdersService.remove_sample(cart, tile))

  
class TilesCountViewSet(BaseViewSet):
  
    def list(self, request):
        cart = CartService.get_cart(request)
        tiles_count = cart.tile_orders.count() + cart.sample_orders.count() + cart.customized_tile_orders.count() + cart.customized_sample_orders.count()
        return Response({'count': tiles_count})


class ShippingCostsViewSet(BaseViewSet):
    
    @list_route(methods=['POST'])
    def shipping_costs(self, request):
        tiles = request.data.get('tiles')
        pickup = request.data.get('pickup')
        delivery = request.data.get('delivery')
        shipping_costs = OrdersService.get_shipping_costs(tiles, pickup, delivery)
        return Response({'shippingCosts': shipping_costs})
       