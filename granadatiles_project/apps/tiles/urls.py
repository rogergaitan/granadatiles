from django.conf.urls import patterns, url
from . import views
from rest_framework.routers import DefaultRouter
from apps.tiles.views import CollectionViewSet, GroupViewSet, TileViewSet, PortfolioViewSet

router = DefaultRouter()
router.register('collections', CollectionViewSet, base_name='collections')
router.register('groups', GroupViewSet, base_name='groups')
router.register('tiles', TileViewSet, base_name='tiles')
router.register('portfolio', PortfolioViewSet, base_name='portfolio')

urlpatterns = router.urls
