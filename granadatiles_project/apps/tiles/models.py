import re
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.dispatch.dispatcher import receiver
from django.conf import settings
from django.core.urlresolvers import reverse
from core.models import BaseGalleryImageModel, BaseCatalogModel, BaseContentModel, BaseSlugModel
from sorl.thumbnail.shortcuts import get_thumbnail
from sorl.thumbnail.fields import ImageField
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Collection(BaseGalleryImageModel, BaseSlugModel):
    menu_image = ImageField(upload_to='Galleries/menu', null = True, blank=True)
    featured = models.BooleanField(default=False, verbose_name=_('Featured'))
    show_in_menu = models.BooleanField(default=False, verbose_name= _('Show in menu'))
    introduction = models.TextField(verbose_name=_('Introduction'), default='')
    introduction_es = models.TextField(blank=True, null=True, verbose_name=_('Introduction_es'))
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)
    uses = models.ManyToManyField('Use', blank=True, related_name='collection', verbose_name=_('Uses'))
    maximum_input_square_foot = models.PositiveIntegerField(null=True, blank=True,
                                                            verbose_name=_('maximum_input_square_foot'))
    minimum_input_square_foot = models.PositiveIntegerField(null=True, blank=True,
                                                            verbose_name=_('minimum_input_square_foot'))

    @property
    def menu_thumbnail(self):
        if self.menu_image:
            return get_thumbnail(self.menu_image, '99x99').url
        return ''

    def get_absolute_url(self, language=None):
        slug = self.get_slug(language)
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


class Group(BaseGalleryImageModel, BaseSlugModel):
    collection = models.ForeignKey(Collection, related_name='groups', verbose_name=_('Collection'))
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)
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
        return reverse('sr-collections:sr-group-detail',
                       kwargs={
                           'group_slug': slug,
                           'collection_slug': self.collection.get_slug(language)
                           })

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')



class TileDesign(BaseCatalogModel):
    group = models.ForeignKey(Group, related_name='designs', verbose_name=_('Tiles Group'))
    styles = models.ManyToManyField('Style', related_name='designs', verbose_name=_('Styles'))
    show_in_web = models.BooleanField(default=True, verbose_name=_('Show in web'))

    def tiles_count(self):
        return self.tiles.count()

    tiles_count.short_description = _('Tiles count')

    class Meta:
        verbose_name = _('Tile Design')
        verbose_name_plural = _('Tile Designs')
        unique_together = ('name', 'group')


class Tile(BaseCatalogModel):
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)
    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)
    sales_price = models.FloatField(verbose_name=_('Sales Price'), blank=True, null=True)
    average_cost = models.FloatField(verbose_name=_('Average Cost'), blank=True, null=True)
    quantity_on_hand = models.IntegerField(verbose_name=_('Quantity'), default=0)
    sales_description = models.CharField(max_length=450 ,verbose_name=_('Sales description'), default='')
    sales_description_es = models.CharField(max_length=450 ,verbose_name=_('Sales description_es'), default='')
    image = ImageField(upload_to='tiles', verbose_name=_('Image'), null = True, blank=True)
    mosaic = ImageField(upload_to='mosaic', verbose_name=_('Mosaic'), null = True, blank=True)
    main = models.BooleanField(default=False, verbose_name=_('Main'),
                               help_text='Is the main tile of the design')
    similar_tiles = models.ManyToManyField('Tile', verbose_name=_('Similar Tiles'), blank=True)
    design = models.ForeignKey(TileDesign, related_name='tiles', verbose_name=_('Design'), null=True, blank = True)
    colors = models.ManyToManyField('PalleteColor', blank=True, related_name='tiles', verbose_name=_('Tiles Colors'))
    is_sample = models.BooleanField(default=False, verbose_name=_('Is Sample'))
    new = models.BooleanField(max_length=10, default=False, verbose_name=_('New'))
    size = models.CharField(max_length=10, default='', null=True, verbose_name=_('Size'))
    height = models.IntegerField(null=True, blank=True, verbose_name=_('Height'))
    width = models.IntegerField(null=True, blank=True, verbose_name=_('Weight'))
    weight = models.CharField(max_length=10, default='', null=True, verbose_name=_('Weight'))
    thickness = models.CharField(max_length=10, default='', null=True, verbose_name=('Thickness'))
    on_sale = models.BooleanField(default=False, verbose_name=_('On Sale'))
    tearsheet = models.FileField(upload_to='tearsheets', null=True, blank=True, verbose_name=_('Tearsheet'))
    custom = models.BooleanField(default=False, blank=True, verbose_name=_('Custom'))
    sample = models.ForeignKey('self', blank=True, null=True, related_name='samples', verbose_name=_('Sample'))
    portfolio = models.ForeignKey('Portfolio', blank=True, null=True, related_name='tiles', verbose_name=_('Portfolio'))
    customized = models.BooleanField(default=False, blank=True, verbose_name=_('Customized'))
    override_collection_box = models.BooleanField(default=False, verbose_name=_('Override Collection Box'))

    def get_sq_ft(self):
        return self.width * self.height * 0.00694444

    def get_price_by_sq_ft(self):
        return (1/self.get_sq_ft()) * self.sales_price

    @property
    def get_admin_url(self):
        return reverse("admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), args=(self.id,))

    def get_available_sizes(self):
        tiles_of_myself = Tile.objects.filter(
            name=self.name, is_sample=False)
        sizes = []
        size =  re.search('\d+"*\s*x\s*\d+"*', self.sales_description)
        sales_description_no_size = self.sales_description.replace(size.group(),'')
        for tile in tiles_of_myself:
            size = re.search('\d+"*\s*x\s*\d+"*', tile.sales_description)
            if tile.sales_description.replace(size.group(),'') == sales_description_no_size:
                sizes.append(tile.size)
        return sizes

    def has_installation_photos(self):
        return (self.installation_photos.count() > 0)

    has_installation_photos.boolean = True


    def has_sample(self):
        return self.sample is not None

    def __str__(self):
        return self.name + ' - ' + self.sales_description

    class Meta:
        verbose_name = _('Tile')
        verbose_name_plural = _('Tiles')


class PalleteColor(BaseCatalogModel):
    hexadecimalCode = models.CharField(max_length=20, verbose_name=_('Color'))

    class Meta:
        verbose_name = _('Pallete Color')
        verbose_name_plural = _('Pallete Colors')


class Style(BaseCatalogModel):

    class Meta:
       verbose_name = _('Style')
       verbose_name_plural = _('Styles')


class Use(BaseCatalogModel):

    class Meta:
       verbose_name = _('Use')
       verbose_name_plural = _('Uses')

class Warehouse(BaseCatalogModel):
    zipcode = models.BooleanField(blank=True, verbose_name=_('Zipcode'))
    custom = models.BooleanField(blank=True, verbose_name=_('Custom'))
    in_stock = models.BooleanField(blank=True, verbose_name=_('In Stock'))

    class Meta:
       verbose_name = _('Warehouse')
       verbose_name_plural = _('Warehouses')


class LeadTime(BaseContentModel):

    class Meta:
       verbose_name = _('Lead Time')
       verbose_name = _('Lead Times')


class Portfolio(models.Model):
    user = models.ForeignKey(User, related_name='portfolio', verbose_name=_('Portfolio'))


class Box(models.Model):
    MEASUREMENT_UNITS = ((1, 'Unit'), (2, 'Square Foot'))

    description = models.CharField(max_length=100, verbose_name=_('Description'))
    measurement_unit = models.PositiveIntegerField(choices=MEASUREMENT_UNITS, verbose_name=_('Measurement Unit'))
    quantity = models.FloatField(verbose_name=_('Quantity'))

    class Meta:
        verbose_name = _('Box')
        verbose_name_plural = _('Boxes')
