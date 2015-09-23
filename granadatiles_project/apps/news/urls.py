from rest_framework.routers import DefaultRouter
from .views import CatalogViewSet, ArticleViewSet

router = DefaultRouter()
router.register('catalogs', CatalogViewSet, base_name='catalogs')
router.register('news/articles', ArticleViewSet, base_name='years')

urlpatterns = router.urls
