from django.contrib.auth.models import User
from django.db.models import Count

from .dtos import ItemCountDto, LatestTilesDto, LatestUsersDto, GroupsByCollectionDto
from apps.tiles.models import Tile, Collection

class ItemCountService():

    def get_item_count():
        itemcountDto = ItemCountDto()
        return itemcountDto


class LatestTilesService():

    def get_latest_tiles(language):
        tiles = Tile.objects.order_by('-id')[:4]
        latesttileDto = [LatestTilesDto(tile, language) for tile in tiles]
        return latesttileDto


class LatestUsersService():

    def get_latest_users():
        users = User.objects.order_by('-id')[:4]
        latestusersDto = [LatestUsersDto(user) for user in users]
        return latestusersDto


class GroupsByCollectionService():

    def get_groups_collection(language):
        colors = [{
            'color': "#f56954",
            'highlight': "#f56954",
            'cssclass': 'text-red'
        },
        {
            'color': "#00a65a",
            'highlight': "#00a65a",
            'cssclass': 'text-green'
        },
        {
            'color': "#f39c12",
            'highlight': "#f39c12",
            'cssclass': 'text-yellow'
        },
        {
            'color': "#00c0ef",
            'highlight': "#00c0ef",
            'cssclass': 'text-aqua'
        },
        {
            'color': "#3c8dbc",
            'highlight': "#3c8dbc",
            'cssclass': 'text-light-blue'
        },
        {
            'color': "#d2d6de",
            'highlight': "#d2d6de",
            'cssclass': 'text-gray'
        }]

        collections = Collection.objects.annotate(group_count=Count('groups')).order_by('-group_count')[:6]
        groupbycollectionDto = [GroupsByCollectionDto(collection, color, language)
                                for collection, color in zip(collections, colors)]

        return groupbycollectionDto
