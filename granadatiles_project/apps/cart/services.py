import math

from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404

from rest_framework.exceptions import APIException

from apps.tiles.models import Tile
from .models import Cart
from .dtos import TileOrdersDto, SampleOrdersDto, CustomizedTileOrdersDto


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
        tile_orders_dto = [TileOrdersDto(tile_order, language) for tile_order in cart.tile_orders.all()]
        return tile_orders_dto

    def get_customized_tile_orders(cart, language):
        customized_tile_orders_dto = [CustomizedTileOrdersDto(customized_tile_order, language)
                                      for customized_tile_order in cart.customized_tile_orders.all()]
        return customized_tile_orders_dto

    def get_sample_orders(cart, language):
        sampleordersdto = [SampleOrdersDto(sampleorder, language) for sampleorder in cart.sample_orders.all()]
        return sampleordersdto

    def tile_quantity(sq_ft, tile):
        return math.ceil(int(sq_ft)/tile.get_sq_ft())

    def get_boxes(tile, quantity):

        if tile.qty_is_sq_ft and tile.box.measurement_unit == 2:
            return math.ceil(quantity/tile.box.quantity)

        if not tile.qty_is_sq_ft and tile.box.measurement_unit == 1:
            return math.ceil(quantity/tile.box.quantity)

        if tile.qty_is_sq_ft and tile.box.measurement_unit == 1:
            return APIException("Cannot use boxes of unit for tiles measure in square foot")

        if not tile.qty_is_sq_ft and tile.box.measurement_unit == 2:
            return APIException("Cannot use boxes of square foot for tiles measure in units")

    def get_subtotal(tile, quantity):
        return quantity * tile.sales_price

    def get_tile(id):
        return get_object_or_404(Tile, list_id=id)

    def add_tile(cart, id, sq_ft):
        tile = CartService.get_tile(id)

        if sq_ft < tile.design.group.collection.minimum_input_square_foot:
            return APIException(_('minimum_input_square_foot_message'))

        if sq_ft > tile.design.group.collection.maximum_input_square_foot:
            return APIException(_('maximum_input_square_foot_message'))

        quantity = CartService.tile_quantity(sq_ft, tile)
        subtotal = CartService.get_subtotal(tile, quantity)
        boxes = CartService.get_boxes(tile, quantity)

        data = {
            'tiles': tile,
            'sq_ft': sq_ft,
            'quantity': quantity,
            'boxes': boxes,
            'subtotal': subtotal
        }

        cart.tile_orders.update_or_create(cart=cart, tiles=tile, defaults=data)

    def remove_tile(cart, id):
        tile = CartService.get_tile(id)
        cart.tile_orders.get(tiles=tile).delete()

    def add_sample(cart, id, quantity):
        tile = CartService.get_tile(id)
        subtotal = int(quantity) * tile.sales_price

        data = {
            'tiles': tile,
            'quantity': quantity,
            'subtotal': subtotal
        }

        cart.sample_orders.update_or_create(cart=cart, tiles=tile, defaults=data)

    def remove_sample(cart, id):
        tile = CartService.get_tile(id)
        cart.sample_orders.get(tiles=tile).delete()

    def save_custom_tile(cart, tile):
        cart.customizedtiles_orders.get()
