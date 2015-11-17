from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tile, Collection, Group
from apps.tiles.models import TileDesign


@admin.register(TileDesign)
class TileDesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es')
    search_fields = ['name', 'name_es']


class TileSizeFilter(admin.SimpleListFilter):

    title = 'tile size available'

    parameter_name = 'size'

    def lookups(self, request, model_admin):
        return(
            ('y', 'Yes'),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.filter(size__isnull=False)

        if self.value() == 'n':
            return queryset.filter(size__isnull=True)


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es', 'sales_description', 'size', 'quantity_on_hand',
                    'list_id', 'is_active', 'new', 'on_sale')
    list_editable = ['size']
    search_fields = ['name', 'name_es', 'list_id', 'size']
    list_filter = ('new', TileSizeFilter)
    actions = ['tile_new']

    def tile_new(self, request, queryset):
        queryset.update(new=True)
    tile_new.short_description = "Mark tile as new"


@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es', 'groups_count', 'featured', 'show_in_menu')
    search_fields = ['title', 'title_es']


@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    list_display = ('title', 'title_es')
    search_fields = ['title', 'title_es']
