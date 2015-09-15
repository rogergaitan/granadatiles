﻿from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class NewsConfig(AppConfig):
    name = 'apps.news'
    verbose_name = _('News')
    icon = 'fa fa-newspaper-o'