from django.db import models
from django.db.models.signals import post_save
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


class TileSize(models.Model):
    weight = models.CharField(max_length=10, verbose_name=_('Weight'))
    thickness = models.CharField(max_length=10, verbose_name=_('Thickness'))

    def __str__(self):
        return "{0} {1}".format(self.weight, self.thickness)

    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Sizes')


class PalleteColor(BaseCatalogModel):
    hexadecimalCode = models.CharField(max_length=20, verbose_name=_('Color'))

    class Meta:
        verbose_name = _('Pallete Color')
        verbose_name_plural = _('Pallete Colors')


class Collection(BaseGalleryImageModel, BaseSlugModel):
    menu_image = ImageField(upload_to='Galleries/menu', null = True, blank=True)
    featured = models.BooleanField(default=True, verbose_name=_('Featured'))
    show_in_menu = models.BooleanField(default=True, verbose_name= _('Show in menu'))
    introduction = models.TextField(verbose_name=_('Introduction'), default='')
    introduction_es = models.TextField(blank=True, null=True, verbose_name=_('Introduction_es'))
    list_id = models.CharField(max_length=30, blank=True, null = True, unique = True)

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
    main = models.BooleanField(default=False, verbose_name=_('Main'),
                               help_text='Is the main tile of the design')
    similar_tiles = models.ManyToManyField('Tile', verbose_name=_('Similar Tiles'), blank=True)
    design = models.ForeignKey(TileDesign, related_name='tiles', verbose_name=_('Design'), null=True, blank = True)
    sizes = models.ManyToManyField(TileSize, related_name='tiles', verbose_name=_('Tiles Sizes'), blank=True)
    colors = models.ManyToManyField(PalleteColor, related_name='tiles', verbose_name=_('Tiles Colors'), blank=True)
    is_sample = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Tile')
        verbose_name_plural = _('Tiles')


class Style(BaseCatalogModel):
    group = models.ForeignKey(Group, related_name='styles', verbose_name=_('Group'))

    class Meta:
       verbose_name = _('Style')
       verbose_name_plural = _('Styles')
