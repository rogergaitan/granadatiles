import requests

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from ...models import Collection, Group, Tile, TileDesign

class Command(BaseCommand):

    def create_update_inventory(item):
        if item['SubLevel'] == 0:
            data = {
                'title':item['Name'],
                'description':'',
                'slug':slugify(item['Name'].split(" ")[0]),
                'list_id':item['ListID']

            }

            Collection.objects.update_or_create(list_id=data['list_id'], defaults=data)

        elif item['SubLevel'] == 1:
            data = {
                'title':item['Name'],
                'description':'',
                'slug':slugify(item['Name']),
                'collection': Collection.objects.get(list_id=item['ParentRef']['ListID']),
                'list_id':item['ListID']

            }

            Group.objects.update_or_create(list_id=data['list_id'], defaults=data)

        elif item['SubLevel'] == 2:
            data = {
                'list_id':item['ListID'],
                'name':item['Name'],
                'is_active':item['IsActive'],
                'sales_price':item['SalesPrice'],
                'quantity_on_hand':item['QuantityOnHand'],
                'average_cost':item['AverageCost'],
                'sales_description':item['SalesDesc'],
                'sales_description_es':item['SalesDesc']

            }

            Tile.objects.update_or_create(list_id=data['list_id'], defaults=data)

            TileDesign.objects.update_or_create(
                name=item['Name'].split(" ")[0],
                defaults = {
                    'name': item['Name'].split(" ")[0],
                    'group': Group.objects.get(list_id=item['ParentRef']['ListID'])
                }

            )


    def handle(self, **options):
        data = {'username': 'qbgtAdmin', 'grant_type': 'password', 'password': 'bkTdHyN6beF8C5cf'}
        response = requests.post('https://granadatilesqbintegration.azurewebsites.net/token', data=data)
        auth = {'Authorization': response.json()['token_type'] + " " + response.json()['access_token']}
        items = requests.get('https://granadatilesqbintegration.azurewebsites.net/api/items', headers=auth)

        collections = [collection for collection in items.json() if collection['SubLevel'] == 0]
        groups = [group for group in items.json() if group['SubLevel'] == 1]
        items = [item for item in items.json() if item['SubLevel'] == 2]

        for collection in collections:
            Command.create_update_inventory(collection)

        for group in groups:
            Command.create_update_inventory(group)

        for item in items:
            Command.create_update_inventory(item)
