from django.db import models
from django.utils.translation import ugettext as _
from core.models import BaseCatalogModel, BaseGalleryImageModel
from sorl.thumbnail.fields import ImageField
from apps.tiles.models import Tile


class Designer(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Designer')
        verbose_name_plural = _('Designers')
        ordering = ['name']


class Photographer(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Photographer')
        verbose_name_plural = _('Photographers')
        ordering = ['name']


class Gallery(BaseCatalogModel):
    image = ImageField(upload_to='Gallery')

    def categories_count(self):
        return str(self.categories.count())

    categories_count.short_description = _('Categories')

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')
        ordering = ['name']


class GalleryCategory(BaseCatalogModel):
    gallery = models.ForeignKey(
        Gallery, verbose_name=_('Gallery'), related_name='categories')

    def images_count(self):
        return str(self.images.count())

    images_count.short_description = _('Images')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']


class GalleryImage(BaseGalleryImageModel):
    gallery_categories = models.ManyToManyField(
        'GalleryCategory', related_name='images',
        verbose_name=_('Gallery Categories'))
    designer = models.ForeignKey(
        Designer, blank=True, null=True, related_name='gallery_images',
        verbose_name=_('Author'))
    photographer = models.ForeignKey(
        Photographer, blank=True, null=True, related_name='gallery_images',
        verbose_name=_('Photographer'))
    tiles = models.ManyToManyField(Tile, blank=True, related_name='installation_photos', verbose_name=_('Tiles'))


    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ['title']
