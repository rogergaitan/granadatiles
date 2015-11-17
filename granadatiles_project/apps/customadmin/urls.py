# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import ItemCountViewSet, LatestTilesViewset, LatestUsersViewSet, GroupsByCollectionViewSet

urlpatterns = patterns('',
    url(r'^search$', 'apps.customadmin.views.search', name="search"),
)

router = DefaultRouter()
router.register('dashboard/itemcounts', ItemCountViewSet, base_name='itemcounts')
router.register('dashboard/latesttiles', LatestTilesViewset, base_name='latesttiles')
router.register('dashboard/latestusers', LatestUsersViewSet, base_name='latestusers')
router.register('dashboard/groupsbycollection', GroupsByCollectionViewSet, base_name='groupsbycollection')


urlpatterns += router.urls
