import math

from django.shortcuts import get_object_or_404

from apps.tiles.models import Tile
from .models import Cart
from .dtos import TileOrdersDto, SampleOrdersDto


class CartService:

    def new(request):
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        return cart

    def get_cart(request):
        cart_id = request.session.get('cart_id')
        if cart_id:
            try:
                cart = Cart.objects.get(pk=cart_id)
            except Cart.DoesNotExist:
                cart = CartService.new(request)
        else:
            cart = CartService.new(request)
        return cart

    def get_tile_orders(cart, language):
        tileordersdto = [TileOrdersDto(tileorder, language) for tileorder in cart.tile_orders.all()]
        return tileordersdto

    def get_sample_orders(cart, language):
        sampleordersdto = [SampleOrdersDto(sampleorder, language) for sampleorder in cart.sample_orders.all()]
        return sampleordersdto

    def tile_quantity(sq_ft, tile):
        quantity = math.ceil(int(sq_ft)/tile.get_sq_ft())
        return quantity

    #def tile_boxes(sq_ft)

    def add_tile(cart, id, sq_ft):
        tile = get_object_or_404(Tile, list_id=id)

        data = {
            'tiles': tile,
            'sq_ft': sq_ft,
            'quantity': CartService.tile_quantity(sq_ft, tile),
            #'boxes': CartService.tile_boxes
        }

        cart.tile_orders.update_or_create(cart=cart, tiles=tile, defaults=data)
