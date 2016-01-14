import math

from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404

from rest_framework.exceptions import APIException

from apps.tiles.models import Tile, CustomizedTile
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

    def tile_quantity(sq_ft, tile):
        return math.ceil(int(sq_ft)/tile.get_sq_ft())

    def get_boxes(tile, quantity):

        if tile.qty_is_sq_ft and tile.box.measurement_unit == 2:
            return math.ceil(quantity/tile.box.quantity)

        if not tile.qty_is_sq_ft and tile.box.measurement_unit == 1:
            return math.ceil(quantity/tile.box.quantity)

        if tile.qty_is_sq_ft and tile.box.measurement_unit == 1:
            raise APIException("Cannot use boxes of unit for tiles measure in square foot")

        if not tile.qty_is_sq_ft and tile.box.measurement_unit == 2:
            raise APIException("Cannot use boxes of square foot for tiles measure in units")

    def get_subtotal(tile, quantity):
        return quantity * tile.sales_price

    def get_tile(id):
        return get_object_or_404(Tile, list_id=id)

    def get_customized_tile(id):
        return get_object_or_404(CustomizedTile, pk=id)

    def get_tile_orders(cart, language):
        tile_orders_dto = [TileOrdersDto(tile_order, language) for tile_order in cart.tile_orders.all()]
        return tile_orders_dto

    def calculate_order(tile, sq_ft):
        if sq_ft < tile.design.group.collection.minimum_input_square_foot:
            raise APIException(_('minimum_input_square_foot_message'))

        if sq_ft > tile.design.group.collection.maximum_input_square_foot:
            raise APIException(_('maximum_input_square_foot_message'))

        quantity = CartService.tile_quantity(sq_ft, tile)
        subtotal = CartService.get_subtotal(tile, quantity)
        boxes = CartService.get_boxes(tile, quantity)

        data = {
            'sq_ft': sq_ft,
            'quantity': quantity,
            'boxes': boxes,
            'subtotal': subtotal
        }

        return data

    def add_tile(cart, tile, sq_ft):
        data = CartService.calculate_order(tile, sq_ft)
        data['tile'] = tile
        cart.tile_orders.update_or_create(cart=cart, tile=tile, defaults=data)

    def remove_tile(cart, tile):
        cart.tile_orders.get(tiles=tile).delete()

    def get_customized_tile_orders(cart, language):
        customized_tile_orders_dto = [CustomizedTileOrdersDto(customized_tile_order, language)
                                      for customized_tile_order in cart.customized_tile_orders.all()]
        return customized_tile_orders_dto

    def add_customized_tile(cart, customized_tile, tile, sq_ft):
        data = CartService.calculate_order(tile, sq_ft)
        data['customized_tile'] = customized_tile
        cart.customized_tile_orders.update_or_create(cart=cart,
                                                    customized_tile=customized_tile,
                                                    defaults=data)

    def remove_customized_tile(cart, customized_tile):
        cart.customizedtiles_orders.get(customized_tile=customized_tile).delete()

    def calculate_sample_order(tile, quantity):
        subtotal = int(quantity) * tile.sales_price

        data = {
            'quantity': quantity,
            'subtotal': subtotal
        }

        return data

    def get_sample_orders(cart, language):
        sample_orders_dto = [SampleOrdersDto(sample_order, language) for sample_order in cart.sample_orders.all()]
        return sample_orders_dto

    def add_sample(cart, tile, quantity):
        data = CartService.calculate_sample_order(tile, quantity)
        data['tile'] = tile
        cart.sample_orders.update_or_create(cart=cart, tile=tile, defaults=data)

    def remove_sample(cart, tile):
        cart.sample_orders.get(tile=tile).delete()

    def get_customized_sample_orders(cart, language):
        customized_sample_orders_dto = [SampleOrdersDto(customized_sample_order, language)
                                        for customized_sample_order in cart.customized_sample_orders.all()]
        return sampleordersdto

    def add_sample_order(cart, customized_tile, tile, quantity):
        data = CartService.calculate_sample_order(tile, quantity)
        data['customized_tile'] = customized_tile
        cart.sample_orders.update_or_create(cart=cart, customized_tile=customized_tile, defaults=data)

    def remove_customized_sample(cart, customized_tile):
        cart.customized_sample_orders.get(customized_tile=customized_tile).delete()
