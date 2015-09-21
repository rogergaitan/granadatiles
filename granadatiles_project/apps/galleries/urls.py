from rest_framework.routers import DefaultRouter
from .views import GalleryViewSet, GalleryCategoryViewSet

router = DefaultRouter()
router.register('galleries', GalleryViewSet, base_name='galleries')
router.register('galleriescategories', GalleryCategoryViewSet, base_name='galleries_categories')

urlpatterns = router.urls
