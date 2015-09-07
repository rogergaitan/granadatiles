from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tile, Collection, Group


@admin.register(Tile)
class TileAdmin(SummernoteModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    pass
