from django.contrib import admin
from .models import Tile, Collection, Group


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
