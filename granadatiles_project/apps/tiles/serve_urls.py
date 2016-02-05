from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _
from apps.tiles.views import collection_detail, group_detail, instock_samples, instock_tiles

urlpatterns = [
    url(_(r'^instock/samples/$'), instock_samples, name='sr-instock-samples' ),
    url(_(r'^instock/tiles/$'), instock_tiles, name='sr-instock-tiles' ),
    url(r'^(?P<slug>[\w-]+)/$', collection_detail, name='sr-detail'),
    url(_(r'^(?P<collection_slug>[\w-]+)/groups/(?P<group_slug>[\w-]+)$'), group_detail, name='sr-group-detail'),

]
