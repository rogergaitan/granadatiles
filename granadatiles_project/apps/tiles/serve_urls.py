from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.tiles.views import collection_detail, group_detail

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', collection_detail, name='sr-detail'),
    url(r'^(?P<slug>[\w-]+)/group/tiles$', group_detail, name='sr-group-detail')
]
