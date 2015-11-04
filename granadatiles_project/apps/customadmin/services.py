from .dtos import ItemCountDto

class ItemCountService(object):

    def get_item_count():
        itemcountDto = ItemCountDto()
        return itemcountDto
