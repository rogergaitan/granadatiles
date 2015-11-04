from django.contrib.auth.models import User

from apps.tiles.models import Collection, Group, Tile


class ItemCountDto():

    def __init__(self):

        self.collections = Collection.objects.count()
        self.groups = Group.objects.count()
        self.tiles = Tile.objects.count()
        self.users = User.objects.count()
