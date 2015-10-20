from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register('quickbooks/items', ItemViewSet, base_name='inventory')

urlpatterns = router.urls
