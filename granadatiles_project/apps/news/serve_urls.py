﻿from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.news.views import news, catalogs
from apps.content.views import videos

urlpatterns = [
    url(_(r'^articles/$'), news, name='sr-news'),
    url(_(r'^videos/$'), videos, name='sr-videos'),
    url(_(r'^catalogs/$'), catalogs, name='sr-catalogs')
]
