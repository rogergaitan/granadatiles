from django.conf.urls import patterns, url
from . import views
from rest_framework.routers import DefaultRouter
from apps.tiles.views import CollectionViewSet, GroupViewSet, TileViewSet, PortfolioTilesViewSet, TaskViewSet

router = DefaultRouter()
router.register('collections', CollectionViewSet, base_name='collections')
router.register('groups', GroupViewSet, base_name='groups')
router.register('tiles', TileViewSet, base_name='tiles')
router.register('portfolio/tiles', PortfolioTilesViewSet, base_name='portfolio_tiles')
router.register('task', TaskViewSet, base_name='tasks')

urlpatterns = router.urls
