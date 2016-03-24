from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import TileOrdersViewSet, TilesCountViewSet, SampleOrdersViewSet, CustomizedTileOrdersViewSet

router = DefaultRouter()
router.register('cart/tiles/count', TilesCountViewSet, base_name='tiles_count')
router.register('cart/tiles', TileOrdersViewSet, base_name='tiles')
router.register('cart/samples', SampleOrdersViewSet, base_name='samples')
router.register('cart/customizedtiles', CustomizedTileOrdersViewSet, base_name='samples')
urlpatterns = router.urls
