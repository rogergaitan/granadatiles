from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from core.views import BaseViewSet
from apps.tiles.models import Tile
from .services import CartService
from .serializers import CartSerializer


class CartViewSet(BaseViewSet):

    @list_route(methods=['get'])
    def show_cart(self, request):
        cart = CartService.get_cart(request, language=self.get_language(request))
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def add_to_cart(self, request):
        tile = Tile.objects.get(list_id=request.query_params['list_id'])
        square_ft = request.query_params['square_ft']


#     def update_square_ft(self, request):



#     def remove_item(self, request):
