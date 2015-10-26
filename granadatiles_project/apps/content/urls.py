from rest_framework.routers import DefaultRouter
from apps.content.views import TestimonyViewSet, SectionViewSet, SocialViewSet, FeaturedVideoViewSet, AreaViewSet, IndexNavigationViewSet

router = DefaultRouter()
router.register('testimonials', TestimonyViewSet, base_name='testimonials')
router.register('sections', SectionViewSet, base_name='sections')
router.register('social_media', SocialViewSet, base_name='social_media')
router.register('videos', FeaturedVideoViewSet, base_name='videos')
router.register('areas', AreaViewSet, base_name='areas')
router.register('index_navigation', IndexNavigationViewSet, base_name='index_navigation')

urlpatterns = router.urls


