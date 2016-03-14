# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import ItemCountViewSet, LatestTilesViewset, LatestUsersViewSet, GroupsByCollectionViewSet, SearchViewSet

router = DefaultRouter()
router.register('dashboard/itemcounts', ItemCountViewSet, base_name='itemcounts')
router.register('dashboard/latesttiles', LatestTilesViewset, base_name='latesttiles')
router.register('dashboard/latestusers', LatestUsersViewSet, base_name='latestusers')
router.register('dashboard/groupsbycollection', GroupsByCollectionViewSet, base_name='groupsbycollection')
router.register('search', SearchViewSet, base_name='search')

urlpatterns = router.urls
