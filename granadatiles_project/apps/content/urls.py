from rest_framework.routers import DefaultRouter
from apps.content.views import TestimonyViewSet

router = DefaultRouter()
router.register('testimonials', TestimonyViewSet, base_name='testimonials')

urlpatterns = router.urls


