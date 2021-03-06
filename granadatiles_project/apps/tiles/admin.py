from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import ugettext as _
from .models import (Tile, Collection, Group, TileDesign, Use, Style, ShippingData,
                     PalleteColor, Warehouse, LeadTime, Box, CustomGroup, TileGroupColor)
from django import forms


class TileInline(admin.StackedInline):
    model = Tile
    fields = ('name', 'name_es')
    readonly_fields = ('name', 'name_es')
    view_on_site = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class TileDesignForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TileDesignForm, self).__init__(*args, **kwargs)
        self.fields['custom_groups'].queryset = CustomGroup.objects.filter(
            collection__id=self.instance.group.collection.id)



@admin.register(TileDesign)
class TileDesignAdmin(admin.ModelAdmin):
    fields = ('name', 'name_es', 'group', 'weight', 'thickness', 'rotate_deg1', 'rotate_deg2', 
              'rotate_deg3', 'rotate_deg4', 'plane', 'styles', 'custom_groups', 'show_in_web')
    list_display = ('name', 'get_collection', 'group', 'tiles_count', 'show_in_web')
    search_fields = ['name', 'name_es', ]
    list_filter = ['show_in_web']
    readonly_fields = ('name', 'group')
    inlines = [TileInline]
    form = TileDesignForm



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
        
class TileImageFilter(admin.SimpleListFilter):
    
    title = _('Image')
    
    parameter_name = 'image'
    
    def lookups(self, request, model_admin):
        return(
            ('y', _('Yes')),
            ('n', 'No')
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'y':
            return queryset.exclude(image='')
        
        if self.value() == 'n':
            return queryset.filter(image='')
    
    
class TileColorGroupInline(admin.TabularInline):
    model = TileGroupColor
    fields = ('color', 'group')
    extra = 12


@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    fields = ('name', 'name_es', 'list_id', 'design', 'sales_description',
              'sales_description_es', 'size', 'height', 'width' ,'sales_price','average_cost', 'qty_is_sq_ft',
              'quantity_on_hand','image', 'mosaic', 'tearsheet', 'box',  'similar_tiles', 'main', 'new', 
              'in_stock', 'is_not_square','is_sample', 'sample', 'override_collection_box', 'is_active', 
              'on_sale')

    list_display = ('name', 'sales_description', 'list_id', 'size', 'quantity_on_hand', 
                    'in_stock', 'qty_is_sq_ft', 'is_active', 'new', 'on_sale')

    list_editable = ['is_active', 'new', 'on_sale', 'size', 'qty_is_sq_ft']
    search_fields = ['name', 'name_es', 'list_id', 'sales_description', 'sales_description_es', 'size']
    list_filter = ('new', CustomTileFilter, TileSizeFilter, TileImageFilter, 'override_collection_box')
    actions = ['tile_new']
    readonly_fields = ('list_id', 'design', 'name', 'quantity_on_hand',
                       'sales_price', 'size', 'average_cost', 'is_sample', 'in_stock')
    inlines = [TileColorGroupInline, ]

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
    
    def save_model(self, request, obj, form, change):
        import_colors = request.POST.get('import_colors')
        if import_colors:
            import_colors = set(import_color.lower() for import_color in import_colors.split(';'))
            for i, v in enumerate(import_colors, 1):
                try:
                    color = PalleteColor.objects.get(name__iexact=v)
                    TileGroupColor.objects.update_or_create(
                        color=color,
                        tile=obj,
                        defaults={'group': 'G{}'.format(i)}
                    )
                except PalleteColor.DoesNotExist:
                    pass
                    
        obj.save()


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
    fields = ('title', 'title_es', 'slug', 'slug_es', 'menu_title', 'menu_title_es', 'list_id', 'description',
              'description_es', 'introduction','introduction_es', 'image', 'menu_image', 'box', 'shipping_data', 
              'uses', 'maximum_input_square_foot', 'minimum_input_square_foot', 'featured', 'show_in_menu')

    list_display = ('title','menu_title', 'groups_count', 'featured', 'show_in_menu')
    search_fields = ['title', 'title_es', 'list_id']
    list_editable = ['featured', 'show_in_menu']
    readonly_fields = ('list_id', )
    inlines = [GroupInline]
    prepopulated_fields = {"slug_es": ("title_es",)}

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        tiles = Tile.objects.filter(design__group__collection__id=obj.id)
        tiles = tiles.exclude(override_collection_box=True)
        boxId = request.POST.get('box', 0)
        if boxId is not 0 and boxId is not '':
            box = Box.objects.get(pk=int(boxId))
            tiles.update(box=box)
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
    fields = ('title', 'title_es', 'slug', 'slug_es', 'list_id', 'collection', 
              'description', 'description_es', 'image', 'show_in_web')

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


@admin.register(CustomGroup)
class CustomGroupAdmin(SummernoteModelAdmin):
    fields = ('title', 'title_es', 'slug', 'slug_es', 'collection', 'description', 
              'description_es', 'order', 'image', 'show_in_web')

    list_display = ('title','collection', 'order', 'show_in_web', 'slug', 'slug_es')
    list_editable = ('order', 'show_in_web')
    search_fields = ['title', 'title_es', 'id']
    prepopulated_fields = {'slug': ('title',), 'slug_es': ('title_es',)}
    
    
@admin.register(ShippingData)
class ShippingDataAdmin(admin.ModelAdmin):
    list_display = ['quantity_uom', 'freigth_class']
