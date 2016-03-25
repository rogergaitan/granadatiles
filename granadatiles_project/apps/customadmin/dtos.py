from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from core.dtos import BaseCatalogDto, BaseContentDto
from apps.tiles.models import Collection, Group, CustomGroup, Tile


class ItemCountDto():

    def __init__(self):
        self.collections = Collection.objects.count()
        self.groups = Group.objects.count()
        self.tiles = Tile.objects.count()
        self.users = User.objects.count()


class LatestTilesDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.image
        self.url = tile.get_admin_url


class LatestUsersDto():

    def __init__(self, user):
        self.name = user.username
        self.url = reverse("admin:%s_%s_change" % (user._meta.app_label, user._meta.model_name), args=(user.id,))


class GroupsByCollectionDto():

    def __init__(self, collection, color, language):
        self.label = collection.get_menu(language) if language else collection.menu_title
        self.value = collection.customgroups.count()
        self.color = color['color']
        self.cssclass = color['cssclass']
        self.highlight = color['highlight']


class SearchDto:

    def __init__(self, search_item, language):
        self.id = search_item.id

        if 'get_name' in dir(search_item):
            self.name = search_item.get_name(language)
        else:
            self.name = search_item.get_title(language)

        self.image = search_item.image.url if search_item.image else ''
        self.type = search_item.__class__.__name__

        if self.type == 'Article':
            self.additional = search_item.magazine.name
            self.additional2 = search_item.date
            self.url = reverse('sr-news:sr-news')
        elif self.type == 'Tile':
            self.additional = search_item.design.group.collection.get_title(language) if search_item.design else '' 
            self.url = search_item.get_absolute_url(language)
        elif self.type == 'CustomGroup':
            self.additional = search_item.collection.get_title(language)
            self.url = search_item.get_absolute_url(language)
        else:
            self.additional = ''

        if self.type != 'Article':
            self.additional2 = ''
