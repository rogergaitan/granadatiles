from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from core.models import BaseCatalogModel

# Other portfolio related models are currently defined on apps.tiles.models
class UserType(BaseCatalogModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('User Type')
        verbose_name_plural = _('User Types')

class UserProfile(models.Model): 
    user = models.OneToOneField(User)
    type = models.ForeignKey(UserType, verbose_name=_('User Type'), related_name='profiles')

    def __str__(self):
        return str(user)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
