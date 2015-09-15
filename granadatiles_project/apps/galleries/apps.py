from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class GalleriesConfig(AppConfig):
    name = 'apps.galleries'
    verbose_name = _('Galleries')
    icon = 'fa fa-picture-o '