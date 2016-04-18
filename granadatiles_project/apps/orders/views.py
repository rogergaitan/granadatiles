from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from core.views import BaseViewSet
from .services import OrdersService


class OrdersViewSet(BaseViewSet):
    
    def create(self, request):
        customer_data = request.data.get('customerData')
        shipping_address = request.data.get('shippingAddress')
        billing_address = request.data.get('billingAddress')
        tiles = request.data.get('tiles')
        customized_tiles = request.data.get('customizedTiles')
        return Response(OrdersService.save_order(customer_data, shipping_address, 
                                                 billing_address, tiles, customized_tiles))
