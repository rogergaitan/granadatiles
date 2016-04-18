from django.contrib.auth.models import User

from .models import Order, OrderDetail, Address
from apps.tiles.models import Tile, CustomizedTile


class OrdersService:
    
    def save_tile_order(customer_data, shipping_address, billing_address, tiles, customized_tiles):
        try:
            user = User.objects.get(pk=customer_data['user'])
        except User.DoesNotExist:
            user = None
        
        order = Order.objects.create(
            customer_first_name=customer_data['customerFirstName'],
            customer_last_name=customer_data['customerLastName'],
            customer_company_name=customer_data['customerCompanyName'],
            credit_card_number=customer_data['creditCardNumber'],
            ip_address=customer_data['ipAddress'],
            user=user,
            same_as_shipping=customer_data['sameAsShipping']
        )
        
        Address.objects.create(
            order=order,
            street_building_house_line1=shipping_address['streetBuildingHouseLine1'],
            house_apt_line2=shipping_address['houseAptLine2'],
            zipcode=shipping_address['zipcode'],
            province_state=shipping_address['provinceState'],
            city=shipping_address['city'],
            type=2            
        )
        
        if customer_data['sameAsShipping'] is False:
            Address.objects.create(
                order=order,
                street_building_house_line1=billing_address['streetBuildingHouseLine1'],
                house_apt_line2=billing_address['houseAptLine2'],
                zipcode=billing_address['zipcode'],
                province_state=billing_address['provinceState'],
                city=billing_address['city'],
                type=1
            )
        
        if tiles:
            for tile_detail in tiles:
                try:
                    tile = Tile.objects.get(pk=tile_detail.id)
                except Tile.DoesNotExist:
                    tile = None
                
                OrderDetail.objects.create(
                    order=order,
                    tile=tile,
                    customized_tile=None,
                    input_sq_ft=tile_detail['inputSqFt'],
                    price_per_sq_feet=tile_detail['pricePerSqFeet'],
                    price_per_tile=tile_detail['pricePerTile'],
                    base_cost=tile_detail['baseCost'],
                    box=tile.box
                )
        if customized_tiles:    
            for customized_tile_detail in customized_tiles:
                try:
                    customized_tile = CustomizedTile.objects.get(pk=customized_tile_detail.id)
                except CustomizedTile.DoesNotExist:
                    customized_tile = None
                    
                OrderDetail.objects.create(
                    order=order,
                    tile=None,
                    customized_tile=customized_tile,
                    input_sq_ft=customized_tile_detail['inputSqFt'],
                    price_per_sq_feet=customized_tile_detail['pricePerSqFeet'],
                    price_per_tile=customized_tile_detail['pricePerTile'],
                    base_cost=customized_tile_detail['baseCost'],
                    box=customized_tile.box
                )