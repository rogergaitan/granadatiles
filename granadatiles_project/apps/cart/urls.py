from rest_framework.routers import DefaultRouter
from .views import TileOrdersViewSet, TilesCountViewSet

router = DefaultRouter()
router.register('cart/tiles', TileOrdersViewSet, base_name='tiles')
router.register('cart/tiles_count', TileOrdersViewSet, base_name='tiles_count')
urlpatterns = router.urls