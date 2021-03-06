﻿from django.db import models
from django.utils.translation import ugettext as _
from core.models import BaseCatalogModel, BaseGalleryImageModel
from sorl.thumbnail.fields import ImageField
from core.managers import BaseDateManager


class Catalog(BaseCatalogModel):
    file = models.FileField(upload_to='Catalogs', verbose_name=_('File'))
    image = models.ImageField(upload_to='Catalog', verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')
        ordering = ['name']

    def __str__(self):
        return self.name
      

class CatalogPage(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='pages', verbose_name=_('Catalog'))
    page_number = models.PositiveIntegerField(verbose_name=_('Page Number'))
    image = ImageField(upload_to='Catalogs/Pages', verbose_name=_('Image'))

    class Meta:
        verbose_name = _('Catalog Page')
        verbose_name_plural = _('Catalog Pages')
        ordering = ['page_number']

    def __str__(self):
        return self.catalog.name


class Magazine(models.Model):
    name = models.CharField(max_length=130, verbose_name=_('Name'))
    logo = models.ImageField(upload_to='Magazines', null=True, blank=True)

    def articles_count(self):
        return str(self.articles.count())

    articles_count.short_description = _('Articles')

    class Meta:
        verbose_name = _('Magazine')
        verbose_name_plural = _('Magazines')
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(BaseGalleryImageModel):
    url = models.URLField(
        max_length=200, verbose_name=_('Link'), null=True, blank=True)
    date = models.DateField(verbose_name=_('Date'))
    magazine = models.ForeignKey(Magazine, related_name='articles')
    file = models.FileField(upload_to='articles_files', null=True, blank=True, verbose_name=_('File'))

    objects = BaseDateManager()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-date']
