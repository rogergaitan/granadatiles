from django.conf.urls import patterns, url
from . import views
from rest_framework.routers import DefaultRouter
from apps.tiles.views import CollectionViewSet

router = DefaultRouter()
router.register('collections', CollectionViewSet, base_name='collections')

urlpatterns = router.urls
