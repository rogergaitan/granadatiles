from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tile, Collection, Group, PalleteColor, TileSize
from apps.tiles.models import TileDesign


@admin.register(TileDesign)
class TileDesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es')
    search_fields = ['name', 'name_es']


def tile_new(modeladmin, request, queryset):
    queryset.update(new=True)
tile_new.short_description = "Mark tile as new"


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es', 'sales_description', 'quantity_on_hand',
                    'list_id', 'is_active', 'new'
                   )
    search_fields = ['name', 'name_es', 'list_id', 'new']
    actions = [tile_new]


@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es', 'groups_count', 'featured', 'show_in_menu')
    search_fields = ['title', 'title_es']


@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es')
    search_fields = ['title', 'title_es']


@admin.register(PalleteColor)
class PalleteColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es')
    search_fields = ['name', 'name_es']


@admin.register(TileSize)
class TileSize(admin.ModelAdmin):
    list_display = ('weight', 'thickness')
