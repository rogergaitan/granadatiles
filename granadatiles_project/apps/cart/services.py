import math
from decimal import Decimal

from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from rest_framework.exceptions import APIException, ValidationError

from apps.tiles.models import Tile, CustomizedTile
from .models import Cart, CustomizedTileOrder, TileOrder
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
            raise ValidationError(_("Cannot use boxes of unit for tiles measure in square foot"))

        if not tile.qty_is_sq_ft and tile.box.measurement_unit == 2:
            raise ValidationError(_("Cannot use boxes of square foot for tiles measure in units"))

    def get_subtotal(tile, quantity):
        return quantity * tile.sales_price

    def calculate_order(tile, sq_ft):
        if sq_ft < tile.design.group.collection.minimum_input_square_foot:
            raise ValidationError(_('The input square footage is less than the minimum input square foot required'))

        if sq_ft > tile.design.group.collection.maximum_input_square_foot:
            raise ValidationError(_('The input square footage is greater than the maximum input square foot required'))

        quantity = OrdersService.tile_quantity(tile, sq_ft + (sq_ft * 0.1))
        subtotal = OrdersService.get_subtotal(tile, quantity)
        boxes = OrdersService.get_boxes(tile, quantity)

        data = {
            'quantity': quantity,
            'boxes': boxes,
            'subtotal': subtotal
        }

        return data
    
    def check_sq_ft(sq_ft, tile):
        """Return collection minimum square foot if sq_ft is empty"""
        if sq_ft is None:
            sq_ft = tile.design.group.collection.minimum_input_square_foot
        else:
            sq_ft = int(sq_ft)
        return sq_ft
      
    def get_tile_orders(cart, language):
        tile_orders_dto = [TileOrdersDto(tile_order, language) for tile_order in cart.tile_orders.all()]
        return tile_orders_dto

    def add_tile_order(request, tile_id, sq_ft):
        cart = CartService.get_cart(request)
        tile = OrdersService.get_tile(tile_id)
        sq_ft = OrdersService.check_sq_ft(sq_ft, tile)
            
        data = OrdersService.calculate_order(tile, sq_ft)
        data['sq_ft'] = sq_ft
        
        cart.tile_orders.update_or_create(
            tile=tile,
	    defaults=data
	)
        
    def update_tile_order(tile_order_id, sq_ft):
        tile_order = get_object_or_404(TileOrder, pk=tile_order_id)
        tile = tile_order.tile
        sq_ft = OrdersService.check_sq_ft(sq_ft, tile)
        
        data = OrdersService.calculate_order(tile, sq_ft)
        
        tile_order.sq_ft = sq_ft
        tile_order.quantity = data['quantity']
        tile_order.boxes = data['boxes']
        tile_order.subtotal = data['subtotal']
        tile_order.save()
            
        return BaseTileOrdersDto(tile_order)
      
    def remove_tile_order(tile_order_id):
        get_object_or_404(TileOrder, pk=tile_order_id).delete()
        
    def get_customized_tile(id):
        return get_object_or_404(CustomizedTile, pk=id)

    def get_customized_tile_orders(cart, language):
        customized_tile_orders_dto = [CustomizedTileOrdersDto(customized_tile_order, language)
                                      for customized_tile_order in cart.customized_tile_orders.all()]
        return customized_tile_orders_dto
    
    def add_customized_tile(request, customized_tile_id, sq_ft):
        cart = CartService.get_cart(request)
        customized_tile = OrdersService.get_customized_tile(customized_tile_id)
        tile = customized_tile.tile
        sq_ft = OrdersService.check_sq_ft(sq_ft, tile)
        
        data = OrdersService.calculate_order(tile, sq_ft)
        data['sq_ft'] = sq_ft
        
        cart.customized_tile_orders.update_or_create(
            customized_tile=customized_tile,
            defaults=data
        )
        
    def update_customized_tile_order(customized_tile_order_id, sq_ft):
        customized_tile_order = CustomizedTileOrder.objects.get(pk=customized_tile_order_id)
        customized_tile = customized_tile_order.customized_tile
        tile = customized_tile.tile
        sq_ft = OrdersService.check_sq_ft(sq_ft, tile)
        
        data = OrdersService.calculate_order(tile, sq_ft)
        
        customized_tile_order.sq_ft = sq_ft
        customized_tile_order.quantity = data['quantity']
        customized_tile_order.boxes = data['boxes']
        customized_tile_order.subtotal = data['subtotal']
        customized_tile_order.save()
        
        return BaseTileOrdersDto(customized_tile_order)

    def remove_customized_tile_order(customized_tile_order_id):
        get_object_or_404(CustomizedTileOrder, pk=customized_tile_order_id).delete()

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

    def get_shipping_costs(orders, pickup_zip, delivery_zip):
        import xml.etree.ElementTree as ET
        
        from suds.client import Client
        import zipcode
        
        try:
            client = Client('https://servicesqa.myblueship.com/BlueGraceService.svc?wsdl')
        except:
            raise APIException(_('An error ocurred please try again'))
        
        shipping_costs = 0
        
        pickup_zip = zipcode.isequal(pickup_zip)
        delivery_zip = zipcode.isequal(delivery_zip)
        
        if pickup_zip is None or delivery_zip is None:
            raise APIException(_('Please enter a valid zip code'))
        
        for order in orders:
           
            tile = Tile.objects.select_related('design__group__collection__shipping_data', 'box').get(pk=order['id'])
            box = tile.box if tile.box else tile.design.group.collection.box

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
                        ).text = ''

            address_pickup = ET.SubElement(pickup, 'Address', {'addressId': ''})
            ET.SubElement(address_pickup, 'City').text = pickup_zip.city.capitalize()
            ET.SubElement(address_pickup, 'StateProvince').text = pickup_zip.state
            ET.SubElement(address_pickup, 'PostalCode').text = pickup_zip.zip
            ET.SubElement(address_pickup, 'CountryCode').text = 'USA'

            delivery = ET.SubElement(quote_request, 'Delivery')

            ET.SubElement(delivery,
                        'Date',
                        {'type':'planned', 'startTime':'10:00', 'endTime': '17:00'},
                        ).text = ''

            address_delivery = ET.SubElement(delivery, 'Address', {'addressId': ''})
            ET.SubElement(address_delivery, 'City').text = delivery_zip.city.capitalize()
            ET.SubElement(address_delivery, 'StateProvince').text = delivery_zip.state
            ET.SubElement(address_delivery, 'PostalCode').text = delivery_zip.zip
            ET.SubElement(address_delivery, 'CountryCode').text = 'USA'

            items = ET.SubElement(quote_request, 'Items')

            item = ET.SubElement(items, 'Item')
            ET.SubElement(item, 'Class').text = tile.design.group.collection.shipping_data.freigth_class
            ET.SubElement(item, 'Weight').text = str(box.weight)
            ET.SubElement(item, 'WeightUom').text = 'lb'
            ET.SubElement(item, 'Quantity').text = str(order['boxes'])
            ET.SubElement(item, 'QuantityUom').text = tile.design.group.collection.shipping_data.quantity_uom

            dimensions = ET.SubElement(item, 'Dimensions')
            ET.SubElement(dimensions, 'Length').text = str(box.length)
            ET.SubElement(dimensions, 'Width').text = str(box.width)
            ET.SubElement(dimensions, 'Height').text = str(box.height)
            ET.SubElement(dimensions, 'Uom').text = 'in'

            request_string = ET.tostring(root, encoding='unicode')
            
            response = client.service.GetQuoteRequestString(request_string)
            root = ET.fromstring(response)
            shipping_costs += Decimal(root[0][3][0][5].text)
        return shipping_costs
