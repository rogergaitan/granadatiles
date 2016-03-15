import math

from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from rest_framework.exceptions import APIException

from apps.tiles.models import Tile, CustomizedTile
from .models import Cart
from .dtos import TileOrdersDto, SampleOrdersDto, CustomizedTileOrdersDto, BaseTileOrdersDto, BaseSampleOrdersDto


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
      
      
class OrdersService:
    
    def get_tile(id):
        return get_object_or_404(Tile, pk=id)
    
    def tile_quantity(tile, sq_ft):
        return math.ceil(sq_ft/tile.get_sq_ft())

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

    def calculate_order(tile, sq_ft):
        if sq_ft < tile.design.group.collection.minimum_input_square_foot:
            raise APIException(_('minimum_input_square_foot_message'))

        if sq_ft > tile.design.group.collection.maximum_input_square_foot:
            raise APIException(_('maximum_input_square_foot_message'))

        quantity = OrdersService.tile_quantity(tile, sq_ft + (sq_ft * 0.1))
        subtotal = OrdersService.get_subtotal(tile, quantity)
        boxes = OrdersService.get_boxes(tile, quantity)

        data = {
            'quantity': quantity,
            'boxes': boxes,
            'subtotal': subtotal
        }

        return data
      
    def get_tile_orders(cart, language):
        tile_orders_dto = [TileOrdersDto(tile_order, language) for tile_order in cart.tile_orders.all()]
        return tile_orders_dto

    def add_tile(cart, tile, sq_ft):
        data = OrdersService.calculate_order(tile, sq_ft)
        data['sq_ft'] = sq_ft
        cart.tile_orders.update_or_create(
            tile=tile,
	    defaults=data
	)
        
    def update_tile(cart, tile, sq_ft):
        data = OrdersService.calculate_order(tile, sq_ft)
        data['sq_ft'] = sq_ft
        tile_order, _ = cart.tile_orders.update_or_create(
            tile=tile,
            defaults=data
        )
        return BaseTileOrdersDto(tile_order)
		      
    def remove_tile(cart, tile):
        cart.tile_orders.get(tile=tile).delete()
        
    def get_customized_tile(id):
        return get_object_or_404(CustomizedTile, pk=id)

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
        data = OrdersService.calculate_sample_order(tile, quantity)
        cart.sample_orders.update_or_create(
            tile=tile,
            defaults=data
        )
	
    def update_sample(cart, tile, quantity):
        data = OrdersService.calculate_sample_order(tile, quantity)
        sample_order, _ = cart.sample_orders.update_or_create(
            tile=tile,
            defaults=data
        )

        return BaseSampleOrdersDto(sample_order)
        
    def remove_sample(cart, tile):
        cart.sample_orders.get(tile=tile).delete()

    def get_customized_sample_orders(cart, language):
        customized_sample_orders_dto = [SampleOrdersDto(customized_sample_order, language)
                                        for customized_sample_order in cart.customized_sample_orders.all()]
        return sampleordersdto

    def add_customized_sample(cart, customized_tile, tile, quantity):
        data = CartService.calculate_sample_order(tile, quantity)
        data['customized_tile'] = customized_tile
        cart.customized_sample_orders.update_or_create(cart=cart, customized_tile=customized_tile, defaults=data)

    def remove_customized_sample(cart, customized_tile):
        cart.customized_sample_orders.get(customized_tile=customized_tile).delete()

    def get_quote_request():
        import xml.etree.ElementTree as ET

        root = ET.Element('QuoteRequests',
                          {'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance',
                           'xmlns:xsd':'http://www.w3.org/2001/XMLSchema',
                           'xmlns':'http://websvcs.myblueship.com/BlueGraceQuoteRequestXML'}
                         )

        quote_request = ET.SubElement(root, 'QuoteRequest')

        ET.SubElement(quote_request,
                      'CustomerName',
                      {'userId':'GranadaWebSvcQA', 'password':'Password1$'}
                     ).text = 'GranadaTiles'

        pickup = ET.SubElement(quote_request, 'PickUp')

        ET.SubElement(pickup,
                      'Date',
                      {'type':'planned', 'startTime':'10:00', 'endTime': '17:00'}
                     ).text = '01/30/16'

        address_pickup = ET.SubElement(pickup, 'Address', {'addressId': ''})
        ET.SubElement(address_pickup, 'City').text = 'Bow'
        ET.SubElement(address_pickup, 'StateProvince').text = 'NH'
        ET.SubElement(address_pickup, 'PostalCode').text = '03304'
        ET.SubElement(address_pickup, 'CountryCode').text = 'USA'

        delivery = ET.SubElement(quote_request, 'Delivery')

        ET.SubElement(delivery,
                      'Date',
                      {'type':'planned', 'startTime':'10:00', 'endTime': '17:00'},
                     ).text = '01/31/06'

        address_delivery = ET.SubElement(delivery, 'Address', {'addressId': ''})
        ET.SubElement(address_delivery, 'City').text = 'RockFord'
        ET.SubElement(address_delivery, 'StateProvince').text = 'IL'
        ET.SubElement(address_delivery, 'PostalCode').text = '61107'
        ET.SubElement(address_delivery, 'CountryCode').text = 'USA'

        items = ET.SubElement(quote_request, 'Items')

        item = ET.SubElement(items, 'Item')
        ET.SubElement(item, 'Class').text = '250'
        ET.SubElement(item, 'Weight').text = '256'
        ET.SubElement(item, 'WeightUom').text = 'lb'
        ET.SubElement(item, 'Quantity').text = '1.0'
        ET.SubElement(item, 'QuantityUom').text = 'PIECES'

        dimensions = ET.SubElement(item, 'Dimensions')
        ET.SubElement(dimensions, 'Length').text = '48.0'
        ET.SubElement(dimensions, 'Width').text = '48.0'
        ET.SubElement(dimensions, 'Height').text = '48.0'
        ET.SubElement(dimensions, 'Uom').text = 'in'

        return ET.tostring(root, encoding='unicode')
      