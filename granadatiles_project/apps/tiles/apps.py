from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TilesConfig(AppConfig):
    name = 'apps.tiles'
    verbose_name = _('Tiles')
    icon = 'fa fa-th'
