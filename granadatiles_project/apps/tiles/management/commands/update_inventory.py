import re
import requests

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

from apps.tiles.models import Collection, Group, Tile, TileDesign

class Command(BaseCommand):

    def create_update_collections(item):
        if re.search('collection', item['Name'], re.I):

            data = {
                'title':item['Name'],
                'description':'',
                'slug':slugify(item['Name'].split(" ")[0]),
                'list_id':item['ListID']
            }

            Collection.objects.update_or_create(list_id=data['list_id'], defaults=data)


    def create_update_groups(item):
        data = {
            'title':item['Name'],
            'description':'',
            'slug':slugify(item['Name']),
            'collection': Collection.objects.get(list_id=item['ParentRef']['ListID']),
            'list_id':item['ListID']
        }

        Group.objects.update_or_create(list_id=data['list_id'], defaults=data)


    def create_update_tiles(item):
        data = {
            'list_id':item['ListID'],
            'name':item['Name'],
            'is_active':item['IsActive'],
            'sales_price':item['SalesPrice'],
            'quantity_on_hand':item['QuantityOnHand'],
            'average_cost':item['AverageCost'],
            'sales_description':item['SalesDesc'],
            'sales_description_es':item['SalesDesc'],
        }


        #get value of samples field
        if re.search('samples', item['FullName'], re.I):
            data['is_sample'] = True

        #get value of custom field
        try:
            group = Group.objects.get(list_id=item['ParentRef']['ListID'])
        except ObjectDoesNotExist:
            group = None

        data['custom'] = False

        if re.search('custom', item['Name'], re.I) or re.search('custom', item['SalesDesc'], re.I):
            data['custom'] = True

        if group and data['custom'] == False and re.search('custom', group.title, re.I):
            data['custom'] = True

        #get value of size field
        data['size'] = ''
        size = re.search('\d+"*\s*x\s*\d+"*', item['SalesDesc'])
        if size: data['size'] = size.group()

        #get height and width
        if data['size']:
            size_width = re.findall('\d+', data['size'])
            data['height'] = size_width[0]
            data['width'] = size_width[1]

        #check quantity square feet
        data['qty_is_sq_ft'] = False
        if re.search('per square foot', item['SalesDesc'], re.I):
            data['qty_is_sq_ft'] = True

        #get tile design
        design = Command.create_update_tiles_designs(item, group)
        if design: data['design'] = design[0]

        Tile.objects.update_or_create(list_id=data['list_id'], defaults=data)


    def create_update_tiles_designs(item, group):

        #add design name from tile
        if re.search('^\d+\s*x\s*\d+', item['Name']):
            design_name = re.search('[a-zA-z]+$', item['Name'])

        elif re.search('\d+\s*x\s*\d+\D*$', item['Name']):
            design_name = re.search('^[a-zA-z]+ [a-zA-z]*', item['Name'])

        else:
            design_name = re.search('\D+\d*', item['Name'])

        if group:

         design = TileDesign.objects.update_or_create(
                      name=design_name.group(),
                      group=group,
                      defaults = {
                          'name': design_name.group(),
                          'group': group
                      }
                  )
         return design


    def handle(self, **options):
        data = {'username': 'qbgtAdmin', 'grant_type': 'password', 'password': 'bkTdHyN6beF8C5cf'}
        response = requests.post('https://granadatilesqbintegration.azurewebsites.net/token', data=data)
        auth = {'Authorization': response.json()['token_type'] + " " + response.json()['access_token']}
        items = requests.get('https://granadatilesqbintegration.azurewebsites.net/api/items', headers=auth)
        collections = [collection for collection in items.json() if collection['SubLevel'] == 0]
        groups = [group for group in items.json() if group['SubLevel'] == 1]
        tiles = [item for item in items.json() if item['SubLevel'] == 2]

        for collection in collections:
            Command.create_update_collections(collection)

        for group in groups:
            Command.create_update_groups(group)
        for tile in tiles:
            Command.create_update_tiles(tile)
