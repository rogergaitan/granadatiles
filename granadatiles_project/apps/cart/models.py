from django.db import models
from django.utils.translation import ugettext as _

from apps.tiles.models import Tile


class Cart(models.Model):

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class TileOrder(models.Model):
    cart = models.ForeignKey(Cart, related_name='tile_orders', verbose_name=_('Tile Orders'))
    tiles = models.ForeignKey(Tile, null=True, blank=True, verbose_name=_('Tiles'))
    sq_ft = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Square feet'))
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity'))
    boxes = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Tile Boxes'))
    subtotal = models.FloatField(null=True, blank=True, verbose_name=_('Subtotal'))

    class Meta:
         verbose_name = _('Tile Order')
         verbose_name_plural = _('Tile Orders')


class SampleOrder(models.Model):
    cart = models.ForeignKey(Cart, related_name='sample_orders', verbose_name=_('Sample Orders'))
    tiles = models.ForeignKey(Tile, null=True, blank=True, verbose_name=_('Tiles'))
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity'))

    class Meta:
         verbose_name = _('Sample Order')
         verbose_name_plural = _('Sample Orders')
