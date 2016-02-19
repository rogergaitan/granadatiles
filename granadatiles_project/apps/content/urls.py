from rest_framework.routers import DefaultRouter
from apps.content.views import TestimonyViewSet, SectionViewSet, SocialViewSet, FeaturedVideoViewSet, AreaViewSet, IndexNavigationViewSet, FlatPageViewSet, CollectionContentViewSet

router = DefaultRouter()
router.register('testimonials', TestimonyViewSet, base_name='testimonials')
router.register('sections', SectionViewSet, base_name='sections')
router.register('flatpages', FlatPageViewSet, base_name='flatpages')
router.register('social_media', SocialViewSet, base_name='social_media')
router.register('videos', FeaturedVideoViewSet, base_name='videos')
router.register('areas', AreaViewSet, base_name='areas')
router.register('index_navigation', IndexNavigationViewSet, base_name='index_navigation')
router.register('collection_content', CollectionContentViewSet, base_name='collection_content')
urlpatterns = router.urls


