from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import ugettext as _
from .models import (Tile, Collection, Group, TileDesign, Use, Style,
                     PalleteColor, Warehouse, LeadTime, Box)


class TileInline(admin.StackedInline):
    model = Tile
    fields = ('name', 'name_es')
    readonly_fields = ('name', 'name_es')
    view_on_site = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TileDesign)
class TileDesignAdmin(admin.ModelAdmin):
    fields = ('name', 'name_es', 'group', 'styles', 'show_in_web')
    list_display = ('name', 'group' , 'tiles_count')
    search_fields = ['name', 'name_es']
    readonly_fields = ('name', 'group')
    inlines = [TileInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TileSizeFilter(admin.SimpleListFilter):

    title = _('tile size available')

    parameter_name = 'size'

    def lookups(self, request, model_admin):
        return(
            ('y', _('Yes')),
            ('n', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.exclude(size='')

        if self.value() == 'n':
            return queryset.filter(size='')


class CustomTileFilter(admin.SimpleListFilter):

    title = _('Custom')

    parameter_name = 'custom'

    def lookups(self, request, model_admin):
        return(
	    ('y', _('Yes')),
	    ('n', 'No')
	)

    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.filter(custom=True)

        if self.value() == 'n':
            return queryset.filter(custom=False)


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    fields = ('name', 'name_es', 'list_id', 'design', 'sales_description',
              'sales_description_es', 'size', 'height', 'width' ,'thickness','weight',
              'sales_price','average_cost', 'quantity_on_hand','image', 'mosaic', 'plane',
              'tearsheet', 'box',  'similar_tiles', 'colors','main', 'new', 'in_stock',
              'is_sample', 'override_collection_box', 'is_active', 'on_sale')

    list_display = ('name', 'sales_description', 'size', 'weight', 'thickness',
                    'quantity_on_hand', 'in_stock', 'is_active', 'new', 'on_sale')

    list_editable = ['is_active', 'new', 'on_sale', 'size', 'weight', 'thickness']
    search_fields = ['name', 'name_es', 'list_id', 'size']
    list_filter = ('new', CustomTileFilter, TileSizeFilter, 'override_collection_box')
    actions = ['tile_new']
    readonly_fields = ('list_id', 'design', 'name', 'quantity_on_hand',
                       'sales_price', 'size', 'average_cost', 'is_sample', 'in_stock')

    def tile_new(self, request, queryset):
        queryset.update(new=True)
    tile_new.short_description = "Mark tile as new"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def in_stock(self, obj):
        return obj.custom is False
    in_stock.boolean = True


class GroupInline(admin.StackedInline):
    model = Group
    fields = ('title', 'title_es')
    readonly_fields = ('title', 'title_es')
    view_on_site = False


    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Collection)
class CollectionAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'list_id', 'description', 'description_es', 'introduction',
              'introduction_es', 'slug', 'slug_es', 'image', 'menu_image', 'box', 'uses',
              'maximum_input_square_foot', 'minimum_input_square_foot', 'featured', 'show_in_menu')

    list_display = ('title', 'groups_count', 'featured', 'show_in_menu')
    search_fields = ['title', 'title_es', 'list_id']
    list_editable = ['featured', 'show_in_menu']
    readonly_fields = ('list_id', 'title')
    inlines = [GroupInline]
    prepopulated_fields = {"slug_es": ("title_es",)}

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        tiles = Tile.objects.filter(design__group__collection__id=obj.id)
        tiles = tiles.filter(override_collection_box=False)
        tiles = tiles.filter(box=True)
        tiles.update(box=request.POST.get('box'))
        obj.save()


class TileDesignInline(admin.StackedInline):
    model = TileDesign
    fields = ('name', 'name_es')
    readonly_fields = ('name', 'name_es')
    view_on_site = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Group)
class GroupAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'list_id', 'collection', 'description', 'description_es',
              'slug', 'slug_es', 'image', 'show_in_web')

    list_display = ('title','collection', 'designs_count', 'tiles_count')
    search_fields = ['title', 'title_es', 'list_id']
    readonly_fields = ('list_id', 'title', 'collection')
    inlines = [TileDesignInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Use)
class UseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'name_es']


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name', 'name_es']


@admin.register(PalleteColor)
class PalleteColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hexadecimalCode', 'order')
    list_editable = ('order',)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'zipcode', 'custom', 'in_stock')
    search_fields = ['name', 'name_es']
    list_filter = ('custom', 'in_stock')


@admin.register(LeadTime)
class LeadTimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        return False


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ('description', 'measurement_unit', 'quantity')
