from django.db import models
from django.utils.translation import ugettext as _
from core.models import BaseCatalogModel, BaseGallerieImageModel
from sorl.thumbnail.fields import ImageField


class Designer(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Designer')
        verbose_name_plural = _('Designers')


class Photographer(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Photographer')
        verbose_name_plural = _('Photographers')


class Gallery(BaseCatalogModel):
    image = ImageField(upload_to='Gallery')

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')


class GalleryCategory(BaseCatalogModel):
    gallery = models.ForeignKey(
        Gallery, verbose_name=_('Gallery'), related_name='categories')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class GalleryImage(BaseGallerieImageModel):
    galleryCategory = models.ForeignKey(
        GalleryCategory, related_name='images',
        verbose_name=_('Gallery Category'))
    designer = models.ForeignKey(
        Designer, blank=True, null=True, related_name='gallery_images',
        verbose_name=_('Author'))
    photographer = models.ForeignKey(
        Photographer, blank=True, null=True, related_name='gallery_images',
        verbose_name=_('Photographer'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
