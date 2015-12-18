import math

from django.utils.translation import ugettext as _
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

    #def get_subtotal()

    def get_tile(id):
        return get_object_or_404(Tile, list_id=id)

    def add_tile(cart, id, sq_ft):
        tile = CartService.get_tile(id)

        if sq_ft < tile.design.group.collection.minimum_input_square_foot:
            return {'message': _('minimum_input_square_foot_message') }

        if sq_ft > tile.design.group.collection.maximum_input_square_foot:
            return {'message': _('maximum_input_square_foot_message') }

        data = {
            'tiles': tile,
            'sq_ft': sq_ft,
            'quantity': CartService.tile_quantity(sq_ft, tile),
            #'boxes': CartService.tile_boxes()
            #'subtotal':
        }

        cart.tile_orders.update_or_create(cart=cart, tiles=tile, defaults=data)

    def remove_tile(cart, id):
        tile = CartService.get_tile(id)
        cart.tile_orders.get(tiles=tile).delete()


    def add_sample(cart, id, quantity):
        tile = CartService.get_tile(id)

        data = {
            'tiles': tile,
            'quantity': quantity,
            #'subtotal':
        }

        cart.sample_orders.update_or_create(cart=cart, tiles=tile, defaults=data)

    def remove_sample(cart, id):
        tile = CartService.get_tile(id)
        cart.sample_orders.get(tiles=tile).delete()
