import requests

from django.core.management.base import BaseCommand, CommandError

from apps.quickbooks.models import Item

class Command(BaseCommand):

    def handle(self, **options):
        data = {'username': 'qbgtAdmin', 'grant_type': 'password', 'password': 'bkTdHyN6beF8C5cf'}
        response = requests.post('https://granadatilesqbintegration.azurewebsites.net/token', data=data)
        auth = {'Authorization': response.json()['token_type'] + " " + response.json()['access_token']}
        items = requests.get('https://granadatilesqbintegration.azurewebsites.net/api/items', headers=auth)

        for item in items.json():

            Item.objects.get_or_create(
                id=item['$id'],
                list_id=item['ListID'],
                name=item['Name'],
                full_name=item['FullName'],
                is_active=item['IsActive'],
                sublevel=item['SubLevel'],
                sales_price=item['SalesPrice'],
                quantity_on_hand=item['QuantityOnHand'],
                average_cost=item['AverageCost'],
                quantity_on_order=item['QuantityOnOrder'],
                quantity_on_sales_order=item['QuantityOnSalesOrder'],
                sales_desc=item['SalesDesc'],
                purchase_desc=item['PurchaseDesc'],
                purchase_cost=item['PurchaseCost'],
            )
