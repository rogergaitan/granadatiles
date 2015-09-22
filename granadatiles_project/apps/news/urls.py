from rest_framework.routers import DefaultRouter
from .views import CatalogViewSet

router = DefaultRouter()
router.register('catalogs', CatalogViewSet, base_name='catalogs')

urlpatterns = router.urls
