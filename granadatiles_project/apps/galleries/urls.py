from rest_framework.routers import DefaultRouter
from .views import GalleryViewSet

router = DefaultRouter()
router.register('galleries', GalleryViewSet, base_name='galleries')

urlpatterns = router.urls
