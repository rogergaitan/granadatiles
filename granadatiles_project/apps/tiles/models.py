from django.db import models
from django.utils.translation import ugettext as _
from core.models import BaseGallerieImageModel, BaseCatalogModel, BaseContentModel, BaseSlugModel
from django.core.urlresolvers import reverse
from sorl.thumbnail.shortcuts import get_thumbnail
from sorl.thumbnail.fields import ImageField


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


class Collection(BaseGallerieImageModel, BaseSlugModel):
    menu_image = ImageField(upload_to='Galleries/menu', null = True, blank=True)
    featured = models.BooleanField(default=True, verbose_name=_('Featured'))
    show_in_menu = models.BooleanField(default=True, verbose_name= _('Show in menu'))

    @property
    def menu_thumbnail(self):
        if self.menu_image:
            return get_thumbnail(self.menu_image, '99x99').url
        return ''

    def get_absolute_url(self, language=None):
        slug = self.get_slug(language)
        return reverse('sr-collections:sr-detail', kwargs={'slug': slug})

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')


class Group(BaseGallerieImageModel):
    collection = models.ForeignKey(Collection, related_name='groups', verbose_name=_('Collection'))

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')



class TileDesign(BaseCatalogModel):
    group = models.ForeignKey(Group, related_name='designs', verbose_name=_('Tiles Group'))

    class Meta:
        verbose_name = _('Tile Design')
        verbose_name_plural = _('Tile Designs')


class Tile(BaseCatalogModel):
    image = ImageField(upload_to='tiles', verbose_name=_('Image'), null = True, blank=True)
    main = models.BooleanField(default=False, verbose_name=_('Main'),
                               help_text='Is the main tile of the design')
    similar_tiles = models.ManyToManyField('Tile', verbose_name=_('Similar Tiles'))
    design = models.ForeignKey(TileDesign, related_name='tiles', verbose_name=_('Design'))
    sizes = models.ManyToManyField(TileSize, related_name='tiles', verbose_name=_('Tiles Sizes'))
    colors = models.ManyToManyField(PalleteColor, related_name='tiles', verbose_name=_('Tiles Colors'))

    class Meta:
        verbose_name = _('Tile')
        verbose_name_plural = _('Tiles')


class Style(BaseCatalogModel):
    group = models.ForeignKey(Group, related_name='styles', verbose_name=_('Group'))

    class Meta:
       verbose_name = _('Style')
       verbose_name_plural = _('Styles')
