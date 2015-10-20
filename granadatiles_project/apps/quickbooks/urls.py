from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register('items', ItemViewSet, base_name='items')

urlpatterns = router.urls
