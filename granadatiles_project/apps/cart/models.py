from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.tiles.models import Tile


class Cart(models.Model):
    square_ft = models.PositiveIntegerField(verbose_name=_('Square feet'))
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    boxes = models.PositiveIntegerField(verbose_name=_('Tile Boxes'))
    tile = models.ForeignKey(Tile, related_name='cart', verbose_name=_('Tile'))
