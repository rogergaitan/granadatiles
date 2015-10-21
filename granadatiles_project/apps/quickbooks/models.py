from django.db import models
from django.utils.translation import ugettext as _
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Item(models.Model):
  list_id = models.CharField(max_length=250)
  name = models.CharField(max_length=250, verbose_name=_('Name'))
  full_name = models.CharField(max_length=250, verbose_name=_('Full name'))
  is_active = models.BooleanField(verbose_name=_('Is Active'))
  sublevel = models.IntegerField(verbose_name=_('Sublevel'))
  sales_price = models.FloatField(verbose_name=_('Sales Price'))
  quantity_on_hand = models.IntegerField(verbose_name=_('Quantity'))
  average_cost = models.FloatField(verbose_name=_('Average Cost'))
  quantity_on_order = models.IntegerField()
  quantity_on_sales_order = models.FloatField()
  sales_desc = models.CharField(max_length=250, verbose_name=_('Sales Description'))
  purchase_desc = models.CharField(max_length=250, verbose_name=_('Purchase Description'))
  purchase_cost = models.FloatField(verbose_name=_('Purchase Cost'))


  def __str__(self):
      return self.name

  class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
