import requests
from .models import Item
from .dtos import ItemDto

class ItemService():

    def get_items():
        items = requests.get('https://granadatilesqbintegration.azurewebsites.net/api/items')
        itemsDto = [ItemDto(item) for item in items.json()]
        return itemsDto
