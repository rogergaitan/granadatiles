from rest_framework.routers import DefaultRouter
from apps.content.views import TestimonyViewSet, SectionViewSet, SocialViewSet

router = DefaultRouter()
router.register('testimonials', TestimonyViewSet, base_name='testimonials')
router.register('sections', SectionViewSet, base_name='sections')
router.register('social_media', SocialViewSet, base_name='social_media')

urlpatterns = router.urls


