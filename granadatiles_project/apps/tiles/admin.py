from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import ugettext as _
from .models import Tile, Collection, Group, TileDesign, Use, Style


@admin.register(TileDesign)
class TileDesignAdmin(admin.ModelAdmin):
    fields = ('name', 'name_es', 'group')
    list_display = ('name', 'name_es')
    search_fields = ['name', 'name_es']
    readonly_fields = ('name', 'group')


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
    fields = ('name', 'name_es', 'list_id', 'design', 'sales_description',
              'sales_description_es', 'size', 'thickness', 'weight',
              'sales_price','average_cost', 'quantity_on_hand',
              'image', 'mosaic', 'similar_tiles', 'colors',
              'is_active', 'main', 'new', 'on_sale', 'is_sample',)

    list_display = ('name', 'sales_description', 'size', 'quantity_on_hand',
                    'is_active', 'new', 'on_sale')

    list_editable = ['is_active', 'new', 'on_sale', 'size']
    search_fields = ['name', 'name_es', 'list_id', 'size']
    list_filter = ('new', TileSizeFilter)
    actions = ['tile_new']
    readonly_fields = ('list_id', 'design', 'name')

    def tile_new(self, request, queryset):
        queryset.update(new=True)
    tile_new.short_description = "Mark tile as new"


@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'list_id', 'description', 'description_es', 'introduction',
              'introduction_es', 'slug', 'slug_es', 'image', 'menu_image', 'uses',
              'featured', 'show_in_menu')

    list_display = ('title', 'groups_count', 'featured', 'show_in_menu')
    search_fields = ['title', 'title_es', 'list_id']
    list_editable = ['featured', 'show_in_menu']
    readonly_fields = ('list_id', 'title')


@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'list_id', 'collection', 'description', 'description_es',
              'slug', 'slug_es', 'image')

    list_display = ('title',)
    search_fields = ['title', 'title_es', 'list_id']
    readonly_fields = ('list_id', 'title', 'collection')


@admin.register(Use)
class UseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'name_es']


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'name_es']
