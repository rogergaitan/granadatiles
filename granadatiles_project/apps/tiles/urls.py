from django.conf.urls import patterns, url
from . import views
from rest_framework.routers import DefaultRouter
from apps.tiles.views import CollectionViewSet, GroupViewSet, TileSizeViewSet

router = DefaultRouter()
router.register('collections', CollectionViewSet, base_name='collections')
router.register('groups', GroupViewSet, base_name='groups')
router.register('sizes', TileSizeViewSet, base_name='sizes')

urlpatterns = router.urls
