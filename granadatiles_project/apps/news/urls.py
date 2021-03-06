from rest_framework.routers import DefaultRouter
from .views import CatalogViewSet, ArticleViewSet

router = DefaultRouter()
router.register('news/catalogs', CatalogViewSet, base_name='catalogs')
router.register('news/articles', ArticleViewSet, base_name='years')
router.register('news', ArticleViewSet, base_name='articles')

urlpatterns = router.urls
