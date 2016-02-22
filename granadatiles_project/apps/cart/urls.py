from rest_framework.routers import DefaultRouter
from .views import TileOrdersViewSet, TilesCountViewSet, SamepleOrdersViewSet

router = DefaultRouter()
router.register('cart/tiles', TileOrdersViewSet, base_name='tiles')
router.register('cart/tiles_count', TilesCountViewSet, base_name='tiles_count')
router.register('cart/samples', SamepleOrdersViewSet, base_name='samples')
urlpatterns = router.urls