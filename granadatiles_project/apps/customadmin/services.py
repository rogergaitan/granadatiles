from django.contrib.auth.models import User

from .dtos import ItemCountDto, LatestTilesDto, LatestUsersDto
from apps.tiles.models import Tile

class ItemCountService(object):

    def get_item_count():
        itemcountDto = ItemCountDto()
        return itemcountDto


class LatestTilesService(object):

    def get_latest_tiles(language):
        tiles = Tile.objects.order_by('-id')[:4]
        latesttileDto = [LatestTilesDto(tile, language) for tile in tiles]
        return latesttileDto


class LatestUsersService(object):

    def get_latest_users():
        users = User.objects.order_by('-id')[:4]
        latestusersDto = [LatestUsersDto(user) for user in users]
        return latestusersDto
