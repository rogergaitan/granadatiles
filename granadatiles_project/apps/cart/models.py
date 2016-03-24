from django.db import models
from django.utils.translation import ugettext as _

from apps.tiles.models import Tile, CustomizedTile


class Cart(models.Model):

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class BaseTileOder(models.Model):
    sq_ft = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Square feet'))
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity'))
    boxes = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Tile Boxes'))
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                   blank=True, verbose_name=_('Subtotal'))

    class Meta:
        abstract = True

class TileOrder(BaseTileOder):
    cart = models.ForeignKey(Cart, related_name='tile_orders', verbose_name=_('Tile Orders'))
    tile = models.ForeignKey(Tile, null=True, blank=True, verbose_name=_('Tiles'))

    class Meta:
         verbose_name = _('Tile Order')
         verbose_name_plural = _('Tile Orders')


class CustomizedTileOrder(BaseTileOder):
    cart = models.ForeignKey(Cart, related_name='customized_tile_orders',
                                       verbose_name=_('Customized Tile Orders'))
    customized_tile = models.ForeignKey(CustomizedTile)


class BaseSampleOrder(models.Model):
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity'))
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                   blank=True, verbose_name=_('Subtotal'))

    class Meta:
        abstract = True

class SampleOrder(BaseSampleOrder):
    cart = models.ForeignKey(Cart, related_name='sample_orders', verbose_name=_('Sample Orders'))
    tile = models.ForeignKey(Tile, null=True, blank=True, verbose_name=_('Tiles'))

    class Meta:
         verbose_name = _('Sample Order')
         verbose_name_plural = _('Sample Orders')


class CustomizedSampleOrder(BaseSampleOrder):
    cart = models.ForeignKey(Cart, related_name='customized_sample_orders',
                                verbose_name=_('Customized Sample Orders'))
    customized_tile = models.ForeignKey(CustomizedTile, verbose_name=_('Customized Tiles'))

    class Meta:
         verbose_name = _('Customized Sample Order')
         verbose_name_plural = _('Customized Sample Orders')
