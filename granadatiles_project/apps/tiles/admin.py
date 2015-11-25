from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import ugettext as _
from .models import Tile, Collection, Group, TileDesign, Use


@admin.register(TileDesign)
class TileDesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es')
    search_fields = ['name', 'name_es']


class TileSizeFilter(admin.SimpleListFilter):

    title = 'tile size available'

    parameter_name = 'size'

    def lookups(self, request, model_admin):
        return(
            ('y', _('Yes')),
            ('n', _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.exclude(size='')

        if self.value() == 'n':
            return queryset.filter(size='')


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es', 'sales_description', 'size', 'quantity_on_hand',
                    'list_id', 'is_active', 'new', 'on_sale')
    list_editable = ['size']
    search_fields = ['name', 'name_es', 'list_id', 'size']
    list_filter = ('new', TileSizeFilter)
    actions = ['tile_new']
    readonly_fields = ('list_id',)

    def tile_new(self, request, queryset):
        queryset.update(new=True)
    tile_new.short_description = "Mark tile as new"


@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'list_id', 'description', 'description_es', 'introduction',
              'introduction_es', 'slug', 'slug_es', 'image', 'menu_image', 'uses',
              'featured', 'show_in_menu'
             )
    list_display = ('title', 'title_es', 'list_id', 'groups_count', 'featured', 'show_in_menu')
    search_fields = ['title', 'title_es', 'list_id']
    readonly_fields = ('list_id', 'title')

@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'list_id', 'collection', 'description', 'description_es',
              'slug', 'slug_es', 'image'
             )
    list_display = ('title', 'title_es', 'list_id')
    search_fields = ['title', 'title_es', 'list_id']
    readonly_fields = ('list_id', 'title', 'collection')


@admin.register(Use)
class UseAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_es')
