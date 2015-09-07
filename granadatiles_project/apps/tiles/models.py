from django.db import models
from django.utils.translation import ugettext as _
from core.models import BaseGallerieImageModel, BaseCatalogModel, BaseContentModel


class TileSize(models.Model):
    weight = models.IntegerField(verbose_name=_('Weight'))
    thickness = models.IntegerField(verbose_name=_('Thickness'))
    
    class Meta:
		verbose_name = _('TileSize')
		verbose_name_plural = _('TileSizes')
	
	
class PalleteColor(BaseCatalogModel):
    hexadecimalCode = models.CharField(max_length=20, verbose_name=_('Color'))
    
    class Meta:
		verbose_name = _('PalleteColor')
		verbose_name_plural = _('PalleteColors')


class Collection(BaseGallerieImageModel):
    
    class Meta:
		verbose_name = _('Collection')
		verbose_name_plural = _('Collections')


class Group(BaseGallerieImageModel):
    collection = models.ForeignKey(Collection, related_name='groups', verbose_name=_('Collection'))

     class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

class Tile(BaseContentModel):
    group = models.ForeignKey(Group, related_name='tiles', verbose_name=_('Tiles Group'))
    sizes = models.ManyToManyField(TileSize, related_name='tiles', verbose_name=_('Tiles Sizes'))
    colors = models.ManyToManyField(PalleteColor, related_name='tiles', verbose_name=_('Tiles Colors'))
    
     class Meta:
        verbose_name = _('Tile')
        verbose_name_plural = _('Tiles')
