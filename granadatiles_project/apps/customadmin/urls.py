# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import ItemCountViewSet

urlpatterns = patterns('',
    url(r'^search$', 'apps.customadmin.views.search', name="search"),
)

router = DefaultRouter()
router.register('dashboard/itemcounts', ItemCountViewSet, base_name='itemcounts')


urlpatterns = router.urls
