from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from core.dtos import BaseCatalogDto, BaseContentDto
from apps.tiles.models import Collection, Group, Tile


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

        self.label = collection.get_title(language) if language else collection.title
        self.value = collection.groups.count()
        self.color = color['color']
        self.cssclass = color['cssclass']
        self.highlight = color['highlight']
