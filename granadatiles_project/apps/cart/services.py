from apps.tiles.models import Tile
from .models import Cart
from .dtos import TileOrdersDto


class CartService:

    def new(request):
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        return cart

    def get_session_cart(request):
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                cart = Cart.objects.get(pk=cart_id)
            except Cart.DoesNotExist:
                cart = CartService.new(request)
        else:
            cart = CartService.new(request)
        return cart

    def show_tile_orders(cart, language):
        tileordersdto = [TileOrdersDto(tileorder, language) for tileorder in cart.tile_orders.all()]
        return tileordersdto
