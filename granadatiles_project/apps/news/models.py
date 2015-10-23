from django.db import models
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

    def __str__(self):
        return self.name


class Magazine(models.Model):
    name = models.CharField(max_length=130, verbose_name=_('Name'))
    logo = models.ImageField(upload_to='Magazines')

    def articles_count(self):
        return str(self.articles.count())

    articles_count.short_description = _('Articulos')

    class Meta:
        verbose_name = _('Magazine')
        verbose_name_plural = _('Magazines')

    def __str__(self):
        return self.name


class Article(BaseGalleryImageModel):
    url = models.URLField(
        max_length=200, verbose_name=_('Link'), null=True, blank=True)
    date = models.DateField(verbose_name=_('Date'))
    magazine = models.ForeignKey(Magazine, related_name='articles')

    objects = BaseDateManager()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
