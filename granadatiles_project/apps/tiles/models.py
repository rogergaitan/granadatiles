import re
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _, activate
from django.dispatch.dispatcher import receiver
from django.conf import settings
from django.core.urlresolvers import reverse
from core.models import BaseGalleryImageModel, BaseCatalogModel, BaseContentModel, BaseSlugModel
from sorl.thumbnail.shortcuts import get_thumbnail
from sorl.thumbnail.fields import ImageField
from rest_framework.authtoken.models import Token
from colorfield.fields import ColorField
from django.utils.functional import cached_property


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_portfolio(sender, instance=None, created=False, **kwargs):
    if created and instance.is_superuser == False:
        Portfolio.objects.create(user=instance)


class Collection(BaseGalleryImageModel, BaseSlugModel):
    menu_title = models.CharField(max_length=200, default='')
    menu_title_es = models.CharField(max_length=200, default='', blank=True)
    menu_image = ImageField(upload_to='Galleries/menu', null = True, blank=True)
    featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    show_in_menu = models.BooleanField(default=False, verbose_name= _('Show in menu'))
    introduction = models.TextField(verbose_name=_('Introduction'), default='')
    introduction_es = models.TextField(blank=True, null=True, verbose_name=_('Introduction_es'))
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)
    uses = models.ManyToManyField('Use', blank=True, related_name='collection', verbose_name=_('Uses'))
    maximum_input_square_foot = models.PositiveIntegerField(default=5000, verbose_name=_('Maximum Input Square Foot'))
    minimum_input_square_foot = models.PositiveIntegerField(default=1, verbose_name=_('Minimum Input Square Foot'))
    box = models.ForeignKey('Box', null=True, blank=True, verbose_name=_('Box'))
    shipping_data = models.ForeignKey('ShippingData', null=True, blank=True, verbose_name=_('Shipping Data'))

    @property
    def menu_thumbnail(self):
        if self.menu_image:
            return get_thumbnail(self.menu_image, '99x99').url
        return ''

    def get_menu(self, language):
        if language == 'es' and self.menu_title_es is not None and self.menu_title_es:
            return self.menu_title_es
        return self.menu_title

    def get_absolute_url(self, language=None):
        slug = self.get_slug(language)
        activate(language)
        return reverse('sr-collections:sr-detail', kwargs={'slug': slug})

    def get_introduction(self, language):
        if language == 'es' and self.introduction_es is not None and self.introduction_es:
            return self.introduction_es
        return self.introduction

    def groups_count(self):
        return str(self.groups.count())

    groups_count.short_description = _('Groups')

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')
        ordering = ['title']
        
        
class BaseGroup(BaseGalleryImageModel, BaseSlugModel):
    collection = models.ForeignKey(Collection, related_name='%(class)ss', verbose_name=_('Collection'))
    show_in_web = models.BooleanField(default=True, verbose_name=_('Show in web'))

    def designs_count(self):
        return self.designs.count()

    def tiles_count(self):
        total = 0
        designs = self.designs.all()
        for design in designs:
            total += design.tiles.count()
        return total

    designs_count.short_description = _('Designs count')
    tiles_count.short_description = _('Tiles count')
    
    def get_absolute_url(self, language=None):
        slug = self.get_slug(language)
        activate(language)
        return reverse('sr-collections:sr-group-detail',
                       kwargs={
                           'group_slug': slug,
                           'collection_slug': self.collection.get_slug(language)
                           })
    
    class Meta:
        abstract = True


class Group(BaseGroup):
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)
   
    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ['title']


class CustomGroup(BaseGroup):
    order = models.PositiveIntegerField(verbose_name=_('Order'))
    
    class Meta:
        verbose_name = _('Custom Group')
        verbose_name_plural = _('Custom Groups')
        ordering = ['order']
        

class TileDesign(BaseCatalogModel):
    ROTATE_DEGREES = (
        (0, '0 deg'),
        (90, '90 deg'),
        (270, '270 deg'),
        (180, '180 deg'),
    )
    
    group = models.ForeignKey(Group, related_name='designs', verbose_name=_('Tiles Group'))
    custom_groups = models.ManyToManyField(CustomGroup, related_name='designs', verbose_name=_('Custom Groups'))
    styles = models.ManyToManyField('Style', related_name='designs', verbose_name=_('Styles'))
    show_in_web = models.BooleanField(default=True, verbose_name=_('Show in web'))
    rotate_deg1 = models.PositiveIntegerField(choices = ROTATE_DEGREES, default = 0)
    rotate_deg2 = models.PositiveIntegerField(choices = ROTATE_DEGREES, default = 90)
    rotate_deg3 = models.PositiveIntegerField(choices = ROTATE_DEGREES, default = 270)
    rotate_deg4 = models.PositiveIntegerField(choices = ROTATE_DEGREES, default = 180)
    plane = models.FileField(upload_to='designs', null= True, blank=True, verbose_name=_('Plane'))
    weight = models.CharField(max_length=10, default='', null=True, verbose_name=_('Weight'))
    thickness = models.CharField(max_length=10, default='', null=True, verbose_name=('Thickness'))

    def tiles_count(self):
        return self.tiles.count()

    def get_collection(self):
        return self.group.collection.title

    tiles_count.short_description = _('Tiles count')
    get_collection.short_description = _('Collection')

    class Meta:
        verbose_name = _('Tile Design')
        verbose_name_plural = _('Tile Designs')
        unique_together = ('name', 'group')
        ordering = ['name']


class Tile(BaseCatalogModel):
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)
    sales_price = models.FloatField(verbose_name=_('Sales Price'), blank=True, null=True)
    average_cost = models.FloatField(verbose_name=_('Average Cost'), blank=True, null=True)
    quantity_on_hand = models.FloatField(verbose_name=_('Quantity'), default=0)
    sales_description = models.CharField(max_length=450 ,verbose_name=_('Sales description'), default='')
    sales_description_es = models.CharField(max_length=450 ,verbose_name=_('Sales description_es'), default='')
    image = ImageField(upload_to='tiles', verbose_name=_('Image'), null=True, blank=True)
    mosaic = ImageField(upload_to='mosaic', verbose_name=_('Mosaic'), null=True, blank=True)
    is_not_square = models.BooleanField(default=False, verbose_name=_('Is Not Square'))
    main = models.BooleanField(default=False, verbose_name=_('Main'),
                               help_text='Is the main tile of the design')
    similar_tiles = models.ManyToManyField('Tile', verbose_name=_('Similar Tiles'), blank=True)
    design = models.ForeignKey(TileDesign, related_name='tiles', verbose_name=_('Design'), null=True, blank = True)
    is_sample = models.BooleanField(default=False, verbose_name=_('Is Sample'))
    new = models.BooleanField(max_length=10, default=False, verbose_name=_('New'))
    size = models.CharField(max_length=10, default='', null=True, verbose_name=_('Size'))
    height = models.IntegerField(null=True, blank=True, verbose_name=_('Height'))
    width = models.IntegerField(null=True, blank=True, verbose_name=_('Width'))
    on_sale = models.BooleanField(default=False, verbose_name=_('On Sale'))
    tearsheet = models.FileField(upload_to='tearsheets', null=True, blank=True, verbose_name=_('Tearsheet'))
    
    custom = models.BooleanField(default=False, blank=True, verbose_name=_('In Stock'))
    sample = models.ForeignKey('self', blank=True, null=True, related_name='samples', verbose_name=_('Sample'))
    override_collection_box = models.BooleanField(default=False, verbose_name=_('Override Collection Box'))
    box = models.ForeignKey('Box', null=True, blank=True, verbose_name=_('Box'))
    qty_is_sq_ft = models.BooleanField(default=False, verbose_name=_('Quantity is in Square Foot'))
    import_colors = models.CharField(max_length=800 , blank=True, null=True,
                                     help_text=_('Warning any input here will override the group colors!'),
                                     verbose_name=_('Import Colors'))

    def get_sq_ft(self):
        if self.qty_is_sq_ft:
           return self.quantity_on_hand
        else:
           width = self.width if self.width else 0
           height = self.height if self.height else 0
           return round(width * height * 0.00694444, 2)

    def get_price_by_sq_ft(self):
        qty_sq = self.get_sq_ft() if self.get_sq_ft() > 0 else 1
        return (1 / qty_sq) * self.sales_price

    @property
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), args=(self.id,))
    
    def get_absolute_url(self, language):
        return self.design.custom_groups.all()[0].get_absolute_url(language) + '?tile='+ str(self.id) if self.design.custom_groups.count() > 0 else ''

    def get_available_sizes(self):
        tiles_of_myself = Tile.objects.filter(name=self.name, is_sample=False)
        sizes = set()
        for tile in tiles_of_myself:
            #check size format, change it if not in standard format
            #if properly formatted use tile size attribute
            size = re.match('(\d+)\s*x\s*(\d+)', tile.size)
            if size:
                size = size.group(1) + '"' + 'x' + size.group(2) + '"' #standardize size format
                sizes.add(size)
            elif tile.size:
                sizes.add(tile.size)
        return sizes

    def has_installation_photos(self):
        return (self.installation_photos.count() > 0)

    has_installation_photos.boolean = True

    def has_sample(self):
        return self.sample is not None

    def in_stock(self):
        return self.custom is False
    
    def get_cart_data(self):
        return {
            'tile_id': self.id
        }       
    
    def __str__(self):
        return self.name + ' - ' + self.sales_description

    class Meta:
        verbose_name = _('Tile')
        verbose_name_plural = _('Tiles')
        ordering = ['name']


class PalleteColor(BaseCatalogModel):
    hexadecimalCode = ColorField(default='#FF0000')
    order = models.PositiveIntegerField(verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Palette Color')
        verbose_name_plural = _('Palette Colors')
        ordering = ['order']


class TileGroupColor(models.Model):
    color = models.ForeignKey(PalleteColor)
    tile = models.ForeignKey(Tile, related_name='colors')
    group = models.CharField(max_length=5)


class Style(BaseCatalogModel):

    class Meta:
       verbose_name = _('Style')
       verbose_name_plural = _('Styles')
       ordering = ['name']


class Use(BaseCatalogModel):

    class Meta:
       verbose_name = _('Use')
       verbose_name_plural = _('Uses')
       ordering = ['name']
       

class Warehouse(BaseCatalogModel):
    zipcode = models.CharField(max_length=5)
    custom = models.BooleanField(blank=True, verbose_name=_('Custom'))
    in_stock = models.BooleanField(blank=True, verbose_name=_('In Stock'))

    class Meta:
       verbose_name = _('Warehouse')
       verbose_name_plural = _('Warehouses')
       ordering = ['name']


class LeadTime(BaseContentModel):

    class Meta:
       verbose_name = _('Lead Time')
       verbose_name_plural = _('Lead Times')
       ordering = ['title']


class Portfolio(models.Model):
    user = models.ForeignKey(User, related_name='portfolio', verbose_name=_('Portfolio'))

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name = _('Portfolios')


class PortfolioTile(models.Model):
    portfolio = models.ForeignKey(Portfolio, related_name='tiles', verbose_name=_('Portfolio'))
    tile = models.ForeignKey(Tile, related_name='portfolio', verbose_name=_('Tile'))

    class Meta:
        verbose_name = _('Portfolio Tile')
        verbose_name_plural = _('Portfolio Tiles')


class Box(models.Model):
    MEASUREMENT_UNITS = ((1, 'Unit'), (2, 'Square Foot'))

    description = models.CharField(max_length=100, verbose_name=_('Description'))
    measurement_unit = models.PositiveIntegerField(choices=MEASUREMENT_UNITS, verbose_name=_('Measurement Unit'))
    quantity = models.FloatField(verbose_name=_('Quantity'))
    weight = models.PositiveIntegerField(default=0, verbose_name=_('Weight'))
    height = models.FloatField(verbose_name=_('Height'))
    length = models.FloatField(verbose_name=_('Lenght'))
    width = models.FloatField(verbose_name=_('Width'))
   
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _('Box')
        verbose_name_plural = _('Boxes')


class Layout(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    length_ft = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Length Ft'))
    length_in = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Length In'))
    width_ft = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Width Ft'))
    width_in = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Width In'))
    image = models.FileField(upload_to='layouts', verbose_name=_('Image'), null=True, blank=True)
    date = models.DateField(auto_now_add=True, verbose_name=_('Date'))
    portfolio = models.ForeignKey(Portfolio, default=False, related_name='layouts', verbose_name=_('Portfolio'))


class CustomizedTile(models.Model):
    tile = models.ForeignKey(Tile, related_name='customizations')
    portfolio = models.ForeignKey(Portfolio, related_name='customized_tiles')
    
    def get_cart_data(self):
        return {
            'customized_tile_id': self.id,
            'tile_id': self.tile.id,
            'group_colors': self.color_groups.all()
        }       
    
    class Meta:
        verbose_name = _('Box')
        verbose_name_plural = _('Boxes')
        
    
class GroupColor(models.Model):
    color = models.ForeignKey(PalleteColor)
    group = models.CharField(max_length=5)
    customized_tile = models.ForeignKey(CustomizedTile, related_name='color_groups')
    
    
class ShippingData(models.Model):
    QUANTITIES_UOM = (
        ('BAG', 'BAG'),
        ('BOXES', 'BOXES'),
        ('BUNDLES', 'BUNDLES'),
        ('CARTONS', 'CARTONS'),
        ('CASES', 'CASES'),
        ('CRATES', 'CRATES'),
        ('DRUMS', 'DRUMS'),
        ('LOOSE', 'LOOSE'),
        ('PAILS', 'PAILS'),
        ('PALLETS', 'PALLETS'),
        ('PIECES', 'PIECES'),
        ('POLES', 'POLES'),
        ('TOTES', 'TOTES'),
        ('ROLLS', 'ROLLS')
    )
    
    FREIGHT_CLASSES = (
        ('50', '50'),
        ('60', '60'),
        ('65', '65'),
        ('70', '70'),
        ('77.5', '77.5'),
        ('85', '85'),
        ('92.5', '92.5'),
        ('100', '100'),
        ('125', '125'),
        ('150', '150'),
        ('175', '175'),
        ('200', '200'),
        ('250', '250'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
    )
    
    quantity_uom = models.CharField(max_length=30, choices=QUANTITIES_UOM, verbose_name=_('Quantity Unit Of Measure'))
    freigth_class = models.CharField(max_length=10, choices=FREIGHT_CLASSES, verbose_name=_('Freight Class'))
    
    def __str__(self):
        return "Quantity Of Measure:{}, Freight Class:{}".format(self.quantity_uom, self.freigth_class)
    
    class Meta:
        verbose_name = _('Shipping Data')
        verbose_name_plural = _('Shipping Data')
