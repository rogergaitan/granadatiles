import requests
from .models import Item
from .dtos import ItemDto

class ItemService():

    def get_items():
        items = Item.objects.all()
        itemsDto = [ItemDto(item) for item in items]
        return itemsDto
