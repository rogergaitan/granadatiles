from django.db import models
from django.utils.translation import ugettext as _

from apps.tiles.models import Tile


class Cart(models.Model):
    square_ft = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Square feet'))
    quantity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Quantity'))
    boxes = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Tile Boxes'))
    tiles = models.ManyToManyField(Tile, related_name='cart', verbose_name=_('Cart'))

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')
