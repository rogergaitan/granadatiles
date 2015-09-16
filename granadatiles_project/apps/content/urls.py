from rest_framework.routers import DefaultRouter
from apps.content.views import TestimonyViewSet, SectionViewSet

router = DefaultRouter()
router.register('testimonials', TestimonyViewSet, base_name='testimonials')
router.register('sections', SectionViewSet, base_name='sections')

urlpatterns = router.urls


