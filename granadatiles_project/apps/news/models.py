from django.db import models
from django.utils.translation import ugettext as _
from core.models import BaseCatalogModel, BaseContentModel
from sorl.thumbnail.fields import ImageField
from core.managers import BaseDateManager

class Catalog(BaseCatalogModel):
    file = models.FileField(upload_to='Catalogs', verbose_name=_('File'))

    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')

    def __str__(self):
        return self.title


class Magazine(models.Model):
    name = models.CharField(max_length=130, verbose_name=_('Name'))
    logo = models.ImageField(upload_to='Magazines')

    class Meta:
        verbose_name = _('Magazine')
        verbose_name_plural = _('Magazines')

    def __str__(self):
        return self.name


class Article(BaseContentModel):
    url = models.CharField(max_length=200, verbose_name=_('Link'), null=True, blank=True)
    date = models.DateField(verbose_name=_('Date'))
    cover = ImageField(upload_to='Magazines')
    magazine = models.ForeignKey(Magazine, related_name='articles')

    objects = BaseDateManager()
    
    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
